import subprocess
import pyfiglet

def suspend_cpanel_account(username, reason="Suspended via script"):
    try:
        result = subprocess.run(
            ['whmapi1', 'suspendacct', f'user={username}', f'reason={reason}'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        if 'result: 1' in result.stdout:
            print(f"✅ Suspended: {username}")
        else:
            print(f"❌ Failed to suspend: {username}\n{result.stdout}")
    except Exception as e:
        print(f"⚠️ Error suspending {username}: {e}")

def main():
    # Display credits using figlet
    credits_figlet = pyfiglet.figlet_format("Shaik Saimeeraa")
    print(credits_figlet)
    print("Founder and CEO, trustedhosting.in, +91-89854-86690\n")

    try:
        with open('usernames.txt', 'r') as file:
            usernames = [line.strip() for line in file if line.strip() and not line.startswith('#')]
    except FileNotFoundError:
        print("❌ 'usernames.txt' not found.")
        return

    for username in usernames:
        suspend_cpanel_account(username)

if __name__ == "__main__":
    main()
