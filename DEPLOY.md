# Deploy notes: gunicorn + systemd

Small Flask app (app.py) with /hello and /webhook.

## What was tested

Tested on Termux (Android), Python 3.13:
- SSH login with a key, a remote command, and scp (to my own phone)
- gunicorn with 2 workers, tested with curl

NOT tested: systemd, a real remote server, nginx, HTTPS.
The steps below are a plan, not proof.

## Steps on a server

1. Log in:

        ssh -i ~/.ssh/mykey user@SERVER_IP

2. Get the code and install:

        git clone REPO_URL
        cd server-deploy-notes
        python3 -m venv venv
        venv/bin/pip install -r requirements.txt

3. Test by hand:

        venv/bin/gunicorn -w 2 -b 127.0.0.1:8000 app:app

4. Make the service file /etc/systemd/system/myapp.service
   (change User and the paths):

        [Unit]
        Description=Orders webhook (gunicorn)
        After=network.target

        [Service]
        User=deploy
        WorkingDirectory=/home/deploy/server-deploy-notes
        ExecStart=/home/deploy/server-deploy-notes/venv/bin/gunicorn -w 2 -b 127.0.0.1:8000 app:app
        Restart=always

        [Install]
        WantedBy=multi-user.target

5. Start it:

        sudo systemctl daemon-reload
        sudo systemctl enable --now myapp
        systemctl status myapp

6. Logs:

        journalctl -u myapp -n 50

7. Update later:

        ssh user@SERVER_IP "cd server-deploy-notes && git pull && sudo systemctl restart myapp"

## Notes

- gunicorn listens on 127.0.0.1 only. To open it to the
  internet, put nginx in front (not done here).
- Use SSH keys with a passphrase on a real server.
