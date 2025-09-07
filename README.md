🖼 Ubuntu-Inspired Image Fetcher

> "I am because we are." – Ubuntu Philosophy



A Python script that lets you fetch and save images from the internet into an organized folder.
Inspired by Ubuntu principles: community, respect, sharing, and practicality.


---

🌍 Features

✅ Fetch images from any valid URL

✅ Automatically create a Fetched_Images/ directory

✅ Extract or generate safe filenames

✅ Save images in binary mode for full quality

✅ Gracefully handle errors and broken links

✅ Prevent duplicate downloads



---

🛠 Requirements

Python 3.7+

Libraries:

pip install requests python-dotenv


(Note: urllib and os are part of Python standard library.)


---

🚀 How to Run

1. Clone this repository:

git clone https://github.com/your-username/Ubuntu_Requests.git
cd Ubuntu_Requests


2. Run the script:

python ubuntu_fetcher.py


3. Enter an image URL when prompted, e.g.:

https://picsum.photos/200/300


4. Your image will be saved in:

Fetched_Images/




---

📸 Example Output

Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter image URL(s): https://picsum.photos/200/300
✓ Successfully fetched: 300
✓ Image saved to Fetched_Images/300

Connection strengthened. Community enriched.


---

🔒 Ubuntu Principles in Code

Community – connects to the global web to fetch shared resources.

Respect – handles failures gracefully without crashing.

Sharing – stores images neatly for reuse.

Practicality – simple, lightweight, and useful.



---

💡 Challenge Extensions

[ ] Support multiple URLs in one run

[ ] Prevent duplicate downloads

[ ] Check HTTP headers before saving

[ ] Security precautions when handling unknown sources



---

📖 License

This project is open-source under the MIT License.
Feel free to fork, improve, and share.
