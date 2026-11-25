# server-deploy-notes

Small Flask webhook app and notes on running it with gunicorn.

## Endpoints
- GET /hello returns a JSON status
- POST /webhook saves an order to test_orders.csv

## Run (tested on Termux, Python 3.13)
    pip install -r requirements.txt
    gunicorn -w 2 -b 127.0.0.1:8000 app:app

## Status
- Tested: gunicorn with 2 workers, checked with curl
- NOT tested: systemd, a real remote server, nginx, HTTPS

See DEPLOY.md for the details and the systemd template.
