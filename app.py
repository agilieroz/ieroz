from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os
import sqlite3

app = Flask(__name__)

BLOG_FILE = 'data/blog.json'
NEWS_FILE = 'data/news.json'

# Fungsi untuk membaca file JSON
def load_posts(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

# Fungsi untuk menyimpan ke file JSON
def save_posts(file_path, posts):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(posts, file, indent=4)

# Halaman Admin untuk posting otomatis
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        return redirect(url_for('add_post'))  # Mengarahkan ke add_post

    blog_posts = load_posts(BLOG_FILE)
    news_posts = load_posts(NEWS_FILE)
    return render_template('admin.html', blog_posts=blog_posts, news_posts=news_posts)

# Route untuk menambahkan post
@app.route('/add_post', methods=['POST'])
def add_post():
    category = request.form.get('category')
    title = request.form.get('title')
    content = request.form.get('content')
    image = request.form.get('image')  # Opsional untuk berita

    if category == 'blog':
        posts = load_posts(BLOG_FILE)
        posts.append({'title': title, 'content': content})
        save_posts(BLOG_FILE, posts)
    elif category == 'news':
        posts = load_posts(NEWS_FILE)
        posts.append({'title': title, 'content': content, 'image': image})
        save_posts(NEWS_FILE, posts)

    return redirect(url_for('admin'))  # Kembali ke halaman admin setelah menambah post

# Halaman Blog
@app.route('/blog')
def blog():
    posts = load_posts(BLOG_FILE)
    return render_template('blog.html', posts=posts)

# Halaman IZ News
@app.route('/news')
def news():
    posts = load_posts(NEWS_FILE)
    return render_template('news.html', posts=posts)

# Rute untuk artikel Blog berdasarkan judul (tanpa hardcode nama file)
@app.route('/blog/<artikel>')
def tampilkan_artikel(artikel):
    return render_template(f'blog/{artikel}')

# Rute untuk berita berdasarkan judul (tanpa hardcode nama file)
@app.route('/news/<news_filename>')
def news_page(news_filename):
    return render_template(f'news/{news_filename}')

@app.route('/about')
def about():
    return render_template('about.html')

CONTACT_FILE = 'data/contacts.json'  # File penyimpanan pesan

# Fungsi untuk membaca pesan dari JSON
def load_contacts():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

# Fungsi untuk menyimpan pesan ke JSON
def save_contact(contact_data):
    contacts = load_contacts()
    contacts.append(contact_data)  # Tambah pesan baru
    with open(CONTACT_FILE, 'w', encoding='utf-8') as file:
        json.dump(contacts, file, indent=4)

# Route untuk halaman kontak (GET: tampilkan, POST: tangani formulir)
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if name and email and message:  # Validasi input
            save_contact({'name': name, 'email': email, 'message': message})
            return redirect(url_for('contact_success'))  # Redirect ke halaman sukses

    return render_template('contact.html')

# Halaman sukses setelah pesan dikirim
@app.route('/contact_success')
def contact_success():
    return render_template('contact_success.html')

# Pastikan folder dan file ada
DATA_FOLDER = "data"
CONTACTS_FILE = os.path.join(DATA_FOLDER, "contacts.json")

if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)  # Buat folder 'data'

if not os.path.exists(CONTACTS_FILE):
    with open(CONTACTS_FILE, 'w', encoding='utf-8') as file:
        json.dump([], file)  # Buat file contacts.json dengan data kosong
        
@app.route('/social')
def social():
    return render_template('social.html')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
