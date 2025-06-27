class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username, email):
        self.users[username] = {"email": email}

    def get_user_email(self, username):
        return self.users.get(username, {}).get("email")

    def send_welcome_email(self, username):
        user_email = self.get_user_email(username)
        if user_email:
            # Sending welcome email (Simulated)
            print(f"Sent welcome email to {user_email}")
    

    def deactivate_user(self, username):
        if username in self.users:
            # Mark the user as deactivated (This was once used but is now deprecated)
            self.users[username]["active"] = False

   
    def get_deactivated_users(self):
        # This method was used to retrieve deactivated users but is no longer used
        return [user for user in self.users if not self.users[user].get("active", True)]


    def send_promotional_email(self, username):
        # This method was used in an old feature that has been replaced
        user_email = self.get_user_email(username)
        if user_email:
            # Sending promotional email (Simulated)
            print(f"Sent promotional email to {user_email}")


def main():
    user_manager = UserManager()
    
    user_manager.add_user("alex", "alex@example.com")
    user_manager.add_user("chris", "chris@example.com")
    
    user_manager.send_welcome_email("alex")
    user_manager.send_welcome_email("chris")
    
    # The following methods are never called and represent dead code
    # user_manager.deactivate_user("alex")
    # user_manager.get_deactivated_users()
    # user_manager.send_promotional_email("chris")

if __name__ == "__main__":
    main()
