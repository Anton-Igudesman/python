import paramiko
import time
import re

class SwitchSSH:
    def __init__(self, hostname, username, password, port=22):
        """
        Initialize SSH connection to a network switch
        
        Args:
            hostname (str): Switch IP or hostname
            username (str): SSH username
            password (str): SSH password
            port (int): SSH port number
        """
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(
            hostname=hostname,
            username=username,
            password=password,
            port=port
        )
        self.shell = self.client.invoke_shell()
        # Wait for initial prompt
        time.sleep(2)
        self.shell.recv(10000).decode('utf-8')
    
    def send_command(self, command, wait_time=2):
        """
        Send a command to the switch and get full output including error messages
        
        Args:
            command (str): Command to execute
            wait_time (float): Time to wait for response
            
        Returns:
            tuple: (output, error_detected)
                - output: Complete command output as string
                - error_detected: Boolean indicating if an error was detected
        """
        # Clear buffer before sending command
        if self.shell.recv_ready():
            self.shell.recv(10000)
            
        # Send command
        self.shell.send(command + '\n')
        
        # Wait for initial response
        time.sleep(wait_time)
        
        # Get complete output
        output = ''
        while self.shell.recv_ready():
            chunk = self.shell.recv(1024).decode('utf-8')
            output += chunk
            time.sleep(0.1)
        
        # Check for various error messages
        error_patterns = [
            r"Unknown command",
            r"Invalid input",
            r"Incomplete command",
            r"Error:",
            r"% Error"
        ]
        
        error_detected = any(re.search(pattern, output, re.IGNORECASE) 
                           for pattern in error_patterns)
        
        return output.strip(), error_detected

    def check_poe_command(self, interface):
        """
        Specific method for handling PoE commands
        
        Args:
            interface (str): Interface identifier
            
        Returns:
            tuple: (success, message)
        """
        command = f"poe port disable {interface}"
        output, error_detected = self.send_command(command)
        
        if error_detected:
            return False, f"Command failed: {output}"
        return True, output

    def close(self):
        """Close SSH connection"""
        self.shell.close()
        self.client.close()

    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()