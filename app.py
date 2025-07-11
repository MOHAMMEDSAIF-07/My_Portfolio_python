from flask import Flask, Response
import os  # Required for environment variables

app = Flask(__name__)

def get_page(page_name):
    pages = {
        "index": '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Portfolio</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary: #2563eb;
            --secondary: #0ea5e9;
            --dark: #1e293b;
            --light: #f8fafc;
            --gray: #94a3b8;
            --accent: #f97316;
            --transition: all 0.3s ease;
            --shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
            --border-radius: 12px;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0f172a, #1e293b);
            color: var(--light);
            line-height: 1.6;
            overflow-x: hidden;
            min-height: 100vh;
        }

        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* Navigation */
        nav {
            position: fixed;
            top: 0;
            width: 100%;
            background: rgba(30, 41, 59, 0.95);
            backdrop-filter: blur(10px);
            z-index: 1000;
            box-shadow: var(--shadow);
        }

        .nav-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 0;
        }

        .logo {
            font-weight: 800;
            font-size: 1.8rem;
            color: var(--light);
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .logo span {
            color: var(--secondary);
        }

        .nav-links {
            display: flex;
            gap: 30px;
        }

        .nav-links a {
            color: var(--gray);
            text-decoration: none;
            font-weight: 500;
            font-size: 1.1rem;
            transition: var(--transition);
            position: relative;
        }

        .nav-links a:hover, .nav-links a.active {
            color: var(--light);
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: var(--secondary);
            transition: var(--transition);
        }

        .nav-links a:hover::after, .nav-links a.active::after {
            width: 100%;
        }

        .mobile-toggle {
            display: none;
            font-size: 1.5rem;
            cursor: pointer;
        }

        /* Page Sections */
        .page {
            min-height: 100vh;
            padding-top: 100px;
            padding-bottom: 80px;
        }

        .section-title {
            font-size: 2.5rem;
            margin-bottom: 50px;
            position: relative;
            display: inline-block;
        }

        .section-title::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 0;
            width: 60px;
            height: 4px;
            background: var(--secondary);
            border-radius: 2px;
        }

        /* Home Section */
        #home {
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            position: relative;
        }

        .hero-content {
            max-width: 800px;
            z-index: 2;
        }

        .hero-title {
            font-size: 4rem;
            font-weight: 800;
            margin-bottom: 20px;
            line-height: 1.2;
        }

        .hero-title span {
            color: var(--secondary);
            display: block;
        }

        .hero-subtitle {
            font-size: 1.5rem;
            color: var(--gray);
            margin-bottom: 30px;
        }

        .cta-button {
            display: inline-block;
            background: var(--primary);
            color: white;
            padding: 14px 40px;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            font-size: 1.1rem;
            transition: var(--transition);
            border: 2px solid var(--primary);
            margin: 10px;
        }

        .cta-button:hover {
            background: transparent;
            transform: translateY(-3px);
            box-shadow: var(--shadow);
        }

        .cta-button.secondary {
            background: transparent;
            border-color: var(--secondary);
        }

        .cta-button.secondary:hover {
            background: var(--secondary);
        }

        /* About Section */
        .about-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
            align-items: center;
        }

        .about-image {
            border-radius: var(--border-radius);
            overflow: hidden;
            box-shadow: var(--shadow);
            position: relative;
        }

        .about-image::before {
            content: '';
            position: absolute;
            top: -20px;
            left: -20px;
            width: 100%;
            height: 100%;
            border: 3px solid var(--secondary);
            border-radius: var(--border-radius);
            z-index: -1;
        }

        .about-image img {
            width: 100%;
            display: block;
            border-radius: var(--border-radius);
        }

        .about-text h3 {
            font-size: 1.8rem;
            margin-bottom: 20px;
            color: var(--secondary);
        }

        .about-text p {
            margin-bottom: 20px;
            color: var(--gray);
        }

        .skills {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin-top: 30px;
        }

        .skill {
            background: rgba(37, 99, 235, 0.1);
            padding: 8px 20px;
            border-radius: 50px;
            font-size: 0.9rem;
            border: 1px solid rgba(37, 99, 235, 0.3);
        }

        /* Education Section */
        .timeline {
            position: relative;
            max-width: 800px;
            margin: 0 auto;
        }

        .timeline::before {
            content: '';
            position: absolute;
            top: 0;
            bottom: 0;
            width: 4px;
            background: var(--secondary);
            left: 50%;
            margin-left: -2px;
        }

        .timeline-item {
            position: relative;
            margin-bottom: 50px;
            width: 50%;
            padding: 20px;
            background: rgba(30, 41, 59, 0.7);
            border-radius: var(--border-radius);
            box-shadow: var(--shadow);
        }

        .timeline-item:nth-child(odd) {
            left: 0;
            text-align: right;
        }

        .timeline-item:nth-child(even) {
            left: 50%;
        }

        .timeline-item::after {
            content: '';
            position: absolute;
            width: 20px;
            height: 20px;
            background: var(--secondary);
            border-radius: 50%;
            top: 30px;
        }

        .timeline-item:nth-child(odd)::after {
            right: -10px;
        }

        .timeline-item:nth-child(even)::after {
            left: -10px;
        }

        .timeline-year {
            color: var(--secondary);
            font-weight: 600;
            margin-bottom: 10px;
        }

        .timeline-title {
            font-size: 1.4rem;
            margin-bottom: 10px;
        }

        .timeline-subtitle {
            color: var(--gray);
            font-style: italic;
        }

        /* Projects Section */
        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 30px;
        }

        .project-card {
            background: rgba(30, 41, 59, 0.7);
            border-radius: var(--border-radius);
            overflow: hidden;
            box-shadow: var(--shadow);
            transition: var(--transition);
        }

        .project-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
        }

        .project-image {
            height: 200px;
            overflow: hidden;
        }

        .project-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: var(--transition);
        }

        .project-card:hover .project-image img {
            transform: scale(1.1);
        }

        .project-content {
            padding: 25px;
        }

        .project-title {
            font-size: 1.4rem;
            margin-bottom: 15px;
        }

        .project-description {
            color: var(--gray);
            margin-bottom: 20px;
        }

        .project-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 20px;
        }

        .project-tag {
            background: rgba(14, 165, 233, 0.1);
            color: var(--secondary);
            padding: 5px 12px;
            border-radius: 50px;
            font-size: 0.8rem;
        }

        .project-link {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            color: var(--secondary);
            text-decoration: none;
            font-weight: 600;
            transition: var(--transition);
        }

        .project-link:hover {
            gap: 12px;
        }

        /* Contact Section */
        .contact-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
        }

        .contact-info {
            display: flex;
            flex-direction: column;
            gap: 30px;
        }

        .contact-item {
            display: flex;
            gap: 20px;
            align-items: flex-start;
        }

        .contact-icon {
            background: rgba(14, 165, 233, 0.1);
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            color: var(--secondary);
            flex-shrink: 0;
        }

        .contact-text h3 {
            margin-bottom: 8px;
            font-size: 1.3rem;
        }

        .contact-text p {
            color: var(--gray);
        }

        .social-links {
            display: flex;
            gap: 20px;
            margin-top: 30px;
        }

        .social-link {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 45px;
            height: 45px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.05);
            color: var(--light);
            font-size: 1.2rem;
            transition: var(--transition);
        }

        .social-link:hover {
            background: var(--secondary);
            transform: translateY(-5px);
        }

        .contact-form {
            background: rgba(30, 41, 59, 0.7);
            padding: 40px;
            border-radius: var(--border-radius);
            box-shadow: var(--shadow);
        }

        .form-group {
            margin-bottom: 25px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 500;
        }

        .form-control {
            width: 100%;
            padding: 14px;
            background: rgba(15, 23, 42, 0.5);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            color: var(--light);
            font-size: 1rem;
            transition: var(--transition);
        }

        .form-control:focus {
            outline: none;
            border-color: var(--secondary);
            background: rgba(15, 23, 42, 0.7);
        }

        textarea.form-control {
            min-height: 150px;
            resize: vertical;
        }

        .submit-btn {
            background: var(--primary);
            color: white;
            border: none;
            padding: 14px 40px;
            border-radius: 50px;
            font-weight: 600;
            font-size: 1.1rem;
            cursor: pointer;
            transition: var(--transition);
            width: 100%;
        }

        .submit-btn:hover {
            background: #1d4ed8;
            transform: translateY(-3px);
        }

        /* Footer */
        footer {
            background: rgba(15, 23, 42, 0.9);
            padding: 30px 0;
            text-align: center;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
        }

        .footer-content {
            color: var(--gray);
            font-size: 0.9rem;
        }

        /* Responsive Design */
        @media (max-width: 992px) {
            .hero-title {
                font-size: 3.2rem;
            }
            
            .about-content,
            .contact-container {
                grid-template-columns: 1fr;
            }
            
            .timeline::before {
                left: 30px;
            }
            
            .timeline-item {
                width: 100%;
                padding-left: 70px;
                padding-right: 25px;
                left: 0 !important;
                text-align: left !important;
            }
            
            .timeline-item:nth-child(odd)::after,
            .timeline-item:nth-child(even)::after {
                left: 20px;
            }
        }

        @media (max-width: 768px) {
            .nav-links {
                position: fixed;
                top: 80px;
                left: 0;
                right: 0;
                background: rgba(30, 41, 59, 0.95);
                flex-direction: column;
                align-items: center;
                padding: 30px 0;
                gap: 25px;
                clip-path: circle(0px at top right);
                transition: clip-path 0.4s ease;
            }
            
            .nav-links.active {
                clip-path: circle(1000px at top right);
            }
            
            .mobile-toggle {
                display: block;
            }
            
            .hero-title {
                font-size: 2.5rem;
            }
            
            .projects-grid {
                grid-template-columns: 1fr;
            }
        }

        @media (max-width: 480px) {
            .hero-title {
                font-size: 2rem;
            }
            
            .section-title {
                font-size: 2rem;
            }
            
            .cta-button {
                display: block;
                margin: 10px auto;
            }
        }
    </style>
</head>
<body>
    <nav>
        <div class="container nav-container">
            <a href="/" class="logo">
                <i class="fas fa-code"></i>MD<span>SAIF</span>
            </a>
            <div class="nav-links">
                <a href="/" class="active">Home</a>
                <a href="/about">About</a>
                <a href="/education">Education</a>
                <a href="/projects">Projects</a>
                <a href="/contact">Contact</a>
            </div>
            <div class="mobile-toggle">
                <i class="fas fa-bars"></i>
            </div>
        </div>
    </nav>

    <section id="home" class="page">
        <div class="container">
            <div class="hero-content">
                <h1 class="hero-title">Hi, I'm <br><span>MOHAMMED SAIF</span></h1>
                <p class="hero-subtitle">PURSUING COMPUTER SCIENCE ENGINEERING</p>
            </div>
        </div>
    </section>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const mobileToggle = document.querySelector('.mobile-toggle');
            const navMenu = document.querySelector('.nav-links');
            
            mobileToggle.addEventListener('click', function() {
                navMenu.classList.toggle('active');
            });
            
            document.addEventListener('click', function(e) {
                if (!e.target.closest('.nav-container') && navMenu.classList.contains('active')) {
                    navMenu.classList.remove('active');
                }
            });
        });
    </script>
</body>
</html>
        ''',

        "about": '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Me</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary: #2563eb;
            --secondary: #0ea5e9;
            --dark: #1e293b;
            --light: #f8fafc;
            --gray: #94a3b8;
            --accent: #f97316;
            --transition: all 0.3s ease;
            --shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
            --border-radius: 12px;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0f172a, #1e293b);
            color: var(--light);
            line-height: 1.6;
            overflow-x: hidden;
            min-height: 100vh;
        }

        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* Navigation */
        nav {
            position: fixed;
            top: 0;
            width: 100%;
            background: rgba(30, 41, 59, 0.95);
            backdrop-filter: blur(10px);
            z-index: 1000;
            box-shadow: var(--shadow);
        }

        .nav-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 0;
        }

        .logo {
            font-weight: 800;
            font-size: 1.8rem;
            color: var(--light);
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .logo span {
            color: var(--secondary);
        }

        .nav-links {
            display: flex;
            gap: 30px;
        }

        .nav-links a {
            color: var(--gray);
            text-decoration: none;
            font-weight: 500;
            font-size: 1.1rem;
            transition: var(--transition);
            position: relative;
        }

        .nav-links a:hover, .nav-links a.active {
            color: var(--light);
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: var(--secondary);
            transition: var(--transition);
        }

        .nav-links a:hover::after, .nav-links a.active::after {
            width: 100%;
        }

        .mobile-toggle {
            display: none;
            font-size: 1.5rem;
            cursor: pointer;
        }

        /* Page Sections */
        .page {
            min-height: 100vh;
            padding-top: 100px;
            padding-bottom: 80px;
        }

        .section-title {
            font-size: 2.5rem;
            margin-bottom: 50px;
            position: relative;
            display: inline-block;
        }

        .section-title::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 0;
            width: 60px;
            height: 4px;
            background: var(--secondary);
            border-radius: 2px;
        }

        /* Home Section */
        #home {
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            position: relative;
        }

        .hero-content {
            max-width: 800px;
            z-index: 2;
        }

        .hero-title {
            font-size: 4rem;
            font-weight: 800;
            margin-bottom: 20px;
            line-height: 1.2;
        }

        .hero-title span {
            color: var(--secondary);
            display: block;
        }

        .hero-subtitle {
            font-size: 1.5rem;
            color: var(--gray);
            margin-bottom: 30px;
        }

        .cta-button {
            display: inline-block;
            background: var(--primary);
            color: white;
            padding: 14px 40px;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            font-size: 1.1rem;
            transition: var(--transition);
            border: 2px solid var(--primary);
            margin: 10px;
        }

        .cta-button:hover {
            background: transparent;
            transform: translateY(-3px);
            box-shadow: var(--shadow);
        }

        .cta-button.secondary {
            background: transparent;
            border-color: var(--secondary);
        }

        .cta-button.secondary:hover {
            background: var(--secondary);
        }

        /* About Section */
        .about-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
            align-items: center;
        }

        .about-image {
            border-radius: var(--border-radius);
            overflow: hidden;
            box-shadow: var(--shadow);
            position: relative;
        }

        .about-image::before {
            content: '';
            position: absolute;
            top: -20px;
            left: -20px;
            width: 100%;
            height: 100%;
            border: 3px solid var(--secondary);
            border-radius: var(--border-radius);
            z-index: -1;
        }

        .about-image img {
            width: 100%;
            display: block;
            border-radius: var(--border-radius);
        }

        .about-text h3 {
            font-size: 1.8rem;
            margin-bottom: 20px;
            color: var(--secondary);
        }

        .about-text p {
            margin-bottom: 20px;
            color: var(--gray);
        }

        .skills {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin-top: 30px;
        }

        .skill {
            background: rgba(37, 99, 235, 0.1);
            padding: 8px 20px;
            border-radius: 50px;
            font-size: 0.9rem;
            border: 1px solid rgba(37, 99, 235, 0.3);
        }

        /* Education Section */
        .timeline {
            position: relative;
            max-width: 800px;
            margin: 0 auto;
        }

        .timeline::before {
            content: '';
            position: absolute;
            top: 0;
            bottom: 0;
            width: 4px;
            background: var(--secondary);
            left: 50%;
            margin-left: -2px;
        }

        .timeline-item {
            position: relative;
            margin-bottom: 50px;
            width: 50%;
            padding: 20px;
            background: rgba(30, 41, 59, 0.7);
            border-radius: var(--border-radius);
            box-shadow: var(--shadow);
        }

        .timeline-item:nth-child(odd) {
            left: 0;
            text-align: right;
        }

        .timeline-item:nth-child(even) {
            left: 50%;
        }

        .timeline-item::after {
            content: '';
            position: absolute;
            width: 20px;
            height: 20px;
            background: var(--secondary);
            border-radius: 50%;
            top: 30px;
        }

        .timeline-item:nth-child(odd)::after {
            right: -10px;
        }

        .timeline-item:nth-child(even)::after {
            left: -10px;
        }

        .timeline-year {
            color: var(--secondary);
            font-weight: 600;
            margin-bottom: 10px;
        }

        .timeline-title {
            font-size: 1.4rem;
            margin-bottom: 10px;
        }

        .timeline-subtitle {
            color: var(--gray);
            font-style: italic;
        }

        /* Projects Section */
        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 30px;
        }

        .project-card {
            background: rgba(30, 41, 59, 0.7);
            border-radius: var(--border-radius);
            overflow: hidden;
            box-shadow: var(--shadow);
            transition: var(--transition);
        }

        .project-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
        }

        .project-image {
            height: 200px;
            overflow: hidden;
        }

        .project-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: var(--transition);
        }

        .project-card:hover .project-image img {
            transform: scale(1.1);
        }

        .project-content {
            padding: 25px;
        }

        .project-title {
            font-size: 1.4rem;
            margin-bottom: 15px;
        }

        .project-description {
            color: var(--gray);
            margin-bottom: 20px;
        }

        .project-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 20px;
        }

        .project-tag {
            background: rgba(14, 165, 233, 0.1);
            color: var(--secondary);
            padding: 5px 12px;
            border-radius: 50px;
            font-size: 0.8rem;
        }

        .project-link {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            color: var(--secondary);
            text-decoration: none;
            font-weight: 600;
            transition: var(--transition);
        }

        .project-link:hover {
            gap: 12px;
        }

        /* Contact Section */
        .contact-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
        }

        .contact-info {
            display: flex;
            flex-direction: column;
            gap: 30px;
        }

        .contact-item {
            display: flex;
            gap: 20px;
            align-items: flex-start;
        }

        .contact-icon {
            background: rgba(14, 165, 233, 0.1);
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            color: var(--secondary);
            flex-shrink: 0;
        }

        .contact-text h3 {
            margin-bottom: 8px;
            font-size: 1.3rem;
        }

        .contact-text p {
            color: var(--gray);
        }

        .social-links {
            display: flex;
            gap: 20px;
            margin-top: 30px;
        }

        .social-link {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 45px;
            height: 45px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.05);
            color: var(--light);
            font-size: 1.2rem;
            transition: var(--transition);
        }

        .social-link:hover {
            background: var(--secondary);
            transform: translateY(-5px);
        }

        .contact-form {
            background: rgba(30, 41, 59, 0.7);
            padding: 40px;
            border-radius: var(--border-radius);
            box-shadow: var(--shadow);
        }

        .form-group {
            margin-bottom: 25px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 500;
        }

        .form-control {
            width: 100%;
            padding: 14px;
            background: rgba(15, 23, 42, 0.5);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            color: var(--light);
            font-size: 1rem;
            transition: var(--transition);
        }

        .form-control:focus {
            outline: none;
            border-color: var(--secondary);
            background: rgba(15, 23, 42, 0.7);
        }

        textarea.form-control {
            min-height: 150px;
            resize: vertical;
        }

        .submit-btn {
            background: var(--primary);
            color: white;
            border: none;
            padding: 14px 40px;
            border-radius: 50px;
            font-weight: 600;
            font-size: 1.1rem;
            cursor: pointer;
            transition: var(--transition);
            width: 100%;
        }

        .submit-btn:hover {
            background: #1d4ed8;
            transform: translateY(-3px);
        }

        /* Footer */
        footer {
            background: rgba(15, 23, 42, 0.9);
            padding: 30px 0;
            text-align: center;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
        }

        .footer-content {
            color: var(--gray);
            font-size: 0.9rem;
        }

        /* Responsive Design */
        @media (max-width: 992px) {
            .hero-title {
                font-size: 3.2rem;
            }
            
            .about-content,
            .contact-container {
                grid-template-columns: 1fr;
            }
            
            .timeline::before {
                left: 30px;
            }
            
            .timeline-item {
                width: 100%;
                padding-left: 70px;
                padding-right: 25px;
                left: 0 !important;
                text-align: left !important;
            }
            
            .timeline-item:nth-child(odd)::after,
            .timeline-item:nth-child(even)::after {
                left: 20px;
            }
        }

        @media (max-width: 768px) {
            .nav-links {
                position: fixed;
                top: 80px;
                left: 0;
                right: 0;
                background: rgba(30, 41, 59, 0.95);
                flex-direction: column;
                align-items: center;
                padding: 30px 0;
                gap: 25px;
                clip-path: circle(0px at top right);
                transition: clip-path 0.4s ease;
            }
            
            .nav-links.active {
                clip-path: circle(1000px at top right);
            }
            
            .mobile-toggle {
                display: block;
            }
            
            .hero-title {
                font-size: 2.5rem;
            }
            
            .projects-grid {
                grid-template-columns: 1fr;
            }
        }

        @media (max-width: 480px) {
            .hero-title {
                font-size: 2rem;
            }
            
            .section-title {
                font-size: 2rem;
            }
            
            .cta-button {
                display: block;
                margin: 10px auto;
            }
        }
    </style>
</head>
<body>
    <nav>
        <div class="container nav-container">
            <a href="/" class="logo">
                <i class="fas fa-code"></i>MD<span>SAIF</span>
            </a>
            <div class="nav-links">
                <a href="/">Home</a>
                <a href="/about" class="active">About</a>
                <a href="/education">Education</a>
                <a href="/projects">Projects</a>
                <a href="/contact">Contact</a>
            </div>
            <div class="mobile-toggle">
                <i class="fas fa-bars"></i>
            </div>
        </div>
    </nav>

    <section id="about" class="page">
        <div class="container">
            <h2 class="section-title">About Me</h2>
            <div class="about-content">
                <div class="about-text">
                    <h3>Computer Science Engineer</h3>
                    <p>Hi, I'm Mohammed Saif, a passionate Computer Science Engineer with a keen interest in software development and web technologies. I am currently pursuing my degree at Muffakham Jah College of Engineering & Technology.</p>
                    <p>I have a strong foundation in programming languages and web development, and I am always eager to learn new technologies and improve my skills. My goal is to create innovative solutions that make a positive impact on people's lives.</p>
                    <div class="skills">
                        <span class="skill">Python</span>
                        <span class="skill">HTML/CSS</span>
                        <span class="skill">MongoDB</span>
                        <span class="skill">RDBMS</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const mobileToggle = document.querySelector('.mobile-toggle');
            const navMenu = document.querySelector('.nav-links');
            
            mobileToggle.addEventListener('click', function() {
                navMenu.classList.toggle('active');
            });
            
            document.addEventListener('click', function(e) {
                if (!e.target.closest('.nav-container') && navMenu.classList.contains('active')) {
                    navMenu.classList.remove('active');
                }
            });
        });
    </script>
</body>
</html>
        ''',

        "education": '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Education</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary: #2563eb;
            --secondary: #0ea5e9;
            --dark: #1e293b;
            --light: #f8fafc;
            --gray: #94a3b8;
            --accent: #f97316;
            --transition: all 0.3s ease;
            --shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
            --border-radius: 12px;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0f172a, #1e293b);
            color: var(--light);
            line-height: 1.6;
            overflow-x: hidden;
            min-height: 100vh;
        }

        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* Navigation */
        nav {
            position: fixed;
            top: 0;
            width: 100%;
            background: rgba(30, 41, 59, 0.95);
            backdrop-filter: blur(10px);
            z-index: 1000;
            box-shadow: var(--shadow);
        }

        .nav-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 0;
        }

        .logo {
            font-weight: 800;
            font-size: 1.8rem;
            color: var(--light);
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .logo span {
            color: var(--secondary);
        }

        .nav-links {
            display: flex;
            gap: 30px;
        }

        .nav-links a {
            color: var(--gray);
            text-decoration: none;
            font-weight: 500;
            font-size: 1.1rem;
            transition: var(--transition);
            position: relative;
        }

        .nav-links a:hover, .nav-links a.active {
            color: var(--light);
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: var(--secondary);
            transition: var(--transition);
        }

        .nav-links a:hover::after, .nav-links a.active::after {
            width: 100%;
        }

        .mobile-toggle {
            display: none;
            font-size: 1.5rem;
            cursor: pointer;
        }

        /* Page Sections */
        .page {
            min-height: 100vh;
            padding-top: 100px;
            padding-bottom: 80px;
        }

        .section-title {
            font-size: 2.5rem;
            margin-bottom: 50px;
            position: relative;
            display: inline-block;
        }

        .section-title::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 0;
            width: 60px;
            height: 4px;
            background: var(--secondary);
            border-radius: 2px;
        }

        /* Home Section */
        #home {
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            position: relative;
        }

        .hero-content {
            max-width: 800px;
            z-index: 2;
        }

        .hero-title {
            font-size: 4rem;
            font-weight: 800;
            margin-bottom: 20px;
            line-height: 1.2;
        }

        .hero-title span {
            color: var(--secondary);
            display: block;
        }

        .hero-subtitle {
            font-size: 1.5rem;
            color: var(--gray);
            margin-bottom: 30px;
        }

        .cta-button {
            display: inline-block;
            background: var(--primary);
            color: white;
            padding: 14px 40px;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            font-size: 1.1rem;
            transition: var(--transition);
            border: 2px solid var(--primary);
            margin: 10px;
        }

        .cta-button:hover {
            background: transparent;
            transform: translateY(-3px);
            box-shadow: var(--shadow);
        }

        .cta-button.secondary {
            background: transparent;
            border-color: var(--secondary);
        }

        .cta-button.secondary:hover {
            background: var(--secondary);
        }

        /* About Section */
        .about-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
            align-items: center;
        }

        .about-image {
            border-radius: var(--border-radius);
            overflow: hidden;
            box-shadow: var(--shadow);
            position: relative;
        }

        .about-image::before {
            content: '';
            position: absolute;
            top: -20px;
            left: -20px;
            width: 100%;
            height: 100%;
            border: 3px solid var(--secondary);
            border-radius: var(--border-radius);
            z-index: -1;
        }

        .about-image img {
            width: 100%;
            display: block;
            border-radius: var(--border-radius);
        }

        .about-text h3 {
            font-size: 1.8rem;
            margin-bottom: 20px;
            color: var(--secondary);
        }

        .about-text p {
            margin-bottom: 20px;
            color: var(--gray);
        }

        .skills {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin-top: 30px;
        }

        .skill {
            background: rgba(37, 99, 235, 0.1);
            padding: 8px 20px;
            border-radius: 50px;
            font-size: 0.9rem;
            border: 1px solid rgba(37, 99, 235, 0.3);
        }

        /* Education Section */
        .timeline {
            position: relative;
            max-width: 800px;
            margin: 0 auto;
        }

        .timeline::before {
            content: '';
            position: absolute;
            top: 0;
            bottom: 0;
            width: 4px;
            background: var(--secondary);
            left: 50%;
            margin-left: -2px;
        }

        .timeline-item {
            position: relative;
            margin-bottom: 50px;
            width: 50%;
            padding: 20px;
            background: rgba(30, 41, 59, 0.7);
            border-radius: var(--border-radius);
            box-shadow: var(--shadow);
        }

        .timeline-item:nth-child(odd) {
            left: 0;
            text-align: right;
        }

        .timeline-item:nth-child(even) {
            left: 50%;
        }

        .timeline-item::after {
            content: '';
            position: absolute;
            width: 20px;
            height: 20px;
            background: var(--secondary);
            border-radius: 50%;
            top: 30px;
        }

        .timeline-item:nth-child(odd)::after {
            right: -10px;
        }

        .timeline-item:nth-child(even)::after {
            left: -10px;
        }

        .timeline-year {
            color: var(--secondary);
            font-weight: 600;
            margin-bottom: 10px;
        }

        .timeline-title {
            font-size: 1.4rem;
            margin-bottom: 10px;
        }

        .timeline-subtitle {
            color: var(--gray);
            font-style: italic;
        }

        /* Projects Section */
        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 30px;
        }

        .project-card {
            background: rgba(30, 41, 59, 0.7);
            border-radius: var(--border-radius);
            overflow: hidden;
            box-shadow: var(--shadow);
            transition: var(--transition);
        }

        .project-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
        }

        .project-image {
            height: 200px;
            overflow: hidden;
        }

        .project-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: var(--transition);
        }

        .project-card:hover .project-image img {
            transform: scale(1.1);
        }

        .project-content {
            padding: 25px;
        }

        .project-title {
            font-size: 1.4rem;
            margin-bottom: 15px;
        }

        .project-description {
            color: var(--gray);
            margin-bottom: 20px;
        }

        .project-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 20px;
        }

        .project-tag {
            background: rgba(14, 165, 233, 0.1);
            color: var(--secondary);
            padding: 5px 12px;
            border-radius: 50px;
            font-size: 0.8rem;
        }

        .project-link {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            color: var(--secondary);
            text-decoration: none;
            font-weight: 600;
            transition: var(--transition);
        }

        .project-link:hover {
            gap: 12px;
        }

        /* Contact Section */
        .contact-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
        }

        .contact-info {
            display: flex;
            flex-direction: column;
            gap: 30px;
        }

        .contact-item {
            display: flex;
            gap: 20px;
            align-items: flex-start;
        }

        .contact-icon {
            background: rgba(14, 165, 233, 0.1);
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            color: var(--secondary);
            flex-shrink: 0;
        }

        .contact-text h3 {
            margin-bottom: 8px;
            font-size: 1.3rem;
        }

        .contact-text p {
            color: var(--gray);
        }

        .social-links {
            display: flex;
            gap: 20px;
            margin-top: 30px;
        }

        .social-link {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 45px;
            height: 45px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.05);
            color: var(--light);
            font-size: 1.2rem;
            transition: var(--transition);
        }

        .social-link:hover {
            background: var(--secondary);
            transform: translateY(-5px);
        }

        .contact-form {
            background: rgba(30, 41, 59, 0.7);
            padding: 40px;
            border-radius: var(--border-radius);
            box-shadow: var(--shadow);
        }

        .form-group {
            margin-bottom: 25px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 500;
        }

        .form-control {
            width: 100%;
            padding: 14px;
            background: rgba(15, 23, 42, 0.5);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            color: var(--light);
            font-size: 1rem;
            transition: var(--transition);
        }

        .form-control:focus {
            outline: none;
            border-color: var(--secondary);
            background: rgba(15, 23, 42, 0.7);
        }

        textarea.form-control {
            min-height: 150px;
            resize: vertical;
        }

        .submit-btn {
            background: var(--primary);
            color: white;
            border: none;
            padding: 14px 40px;
            border-radius: 50px;
            font-weight: 600;
            font-size: 1.1rem;
            cursor: pointer;
            transition: var(--transition);
            width: 100%;
        }

        .submit-btn:hover {
            background: #1d4ed8;
            transform: translateY(-3px);
        }

        /* Footer */
        footer {
            background: rgba(15, 23, 42, 0.9);
            padding: 30px 0;
            text-align: center;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
        }

        .footer-content {
            color: var(--gray);
            font-size: 0.9rem;
        }

        /* Responsive Design */
        @media (max-width: 992px) {
            .hero-title {
                font-size: 3.2rem;
            }
            
            .about-content,
            .contact-container {
                grid-template-columns: 1fr;
            }
            
            .timeline::before {
                left: 30px;
            }
            
            .timeline-item {
                width: 100%;
                padding-left: 70px;
                padding-right: 25px;
                left: 0 !important;
                text-align: left !important;
            }
            
            .timeline-item:nth-child(odd)::after,
            .timeline-item:nth-child(even)::after {
                left: 20px;
            }
        }

        @media (max-width: 768px) {
            .nav-links {
                position: fixed;
                top: 80px;
                left: 0;
                right: 0;
                background: rgba(30, 41, 59, 0.95);
                flex-direction: column;
                align-items: center;
                padding: 30px 0;
                gap: 25px;
                clip-path: circle(0px at top right);
                transition: clip-path 0.4s ease;
            }
            
            .nav-links.active {
                clip-path: circle(1000px at top right);
            }
            
            .mobile-toggle {
                display: block;
            }
            
            .hero-title {
                font-size: 2.5rem;
            }
            
            .projects-grid {
                grid-template-columns: 1fr;
            }
        }

        @media (max-width: 480px) {
            .hero-title {
                font-size: 2rem;
            }
            
            .section-title {
                font-size: 2rem;
            }
            
            .cta-button {
                display: block;
                margin: 10px auto;
            }
        }
    </style>
</head>
<body>
    <nav>
        <div class="container nav-container">
            <a href="/" class="logo">
                <i class="fas fa-code"></i>MD<span>SAIF</span>
            </a>
            <div class="nav-links">
                <a href="/">Home</a>
                <a href="/about">About</a>
                <a href="/education" class="active">Education</a>
                <a href="/projects">Projects</a>
                <a href="/contact">Contact</a>
            </div>
            <div class="mobile-toggle">
                <i class="fas fa-bars"></i>
            </div>
        </div>
    </nav>

    <section id="education" class="page">
        <div class="container">
            <h2 class="section-title">Education</h2>
            <div class="timeline">
                <div class="timeline-item">
                    <div class="timeline-year">2022 - 2025 (Diploma)</div>
                    <h3 class="timeline-title">Computer Science Engineering</h3>
                    <p class="timeline-subtitle">BGTI - Brilliant Group of Technical Institutions</p>
                </div>
                <div class="timeline-item">
                    <div class="timeline-year">2025 - 2028 (B.Tech)</div>
                    <h3 class="timeline-title">Computer Science Engineering</h3>
                    <p class="timeline-subtitle">MJCET - Muffakham Jah College of Engineering & Technology (PURSUING)</p>
                </div>
            </div>
        </div>
    </section>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const mobileToggle = document.querySelector('.mobile-toggle');
            const navMenu = document.querySelector('.nav-links');
            
            mobileToggle.addEventListener('click', function() {
                navMenu.classList.toggle('active');
            });
            
            document.addEventListener('click', function(e) {
                if (!e.target.closest('.nav-container') && navMenu.classList.contains('active')) {
                    navMenu.classList.remove('active');
                }
            });
        });
    </script>
</body>
</html>
        ''',

        "projects": '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Projects</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary: #2563eb;
            --secondary: #0ea5e9;
            --dark: #1e293b;
            --light: #f8fafc;
            --gray: #94a3b8;
            --accent: #f97316;
            --transition: all 0.3s ease;
            --shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
            --border-radius: 12px;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0f172a, #1e293b);
            color: var(--light);
            line-height: 1.6;
            overflow-x: hidden;
            min-height: 100vh;
        }

        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* Navigation */
        nav {
            position: fixed;
            top: 0;
            width: 100%;
            background: rgba(30, 41, 59, 0.95);
            backdrop-filter: blur(10px);
            z-index: 1000;
            box-shadow: var(--shadow);
        }

        .nav-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 0;
        }

        .logo {
            font-weight: 800;
            font-size: 1.8rem;
            color: var(--light);
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .logo span {
            color: var(--secondary);
        }

        .nav-links {
            display: flex;
            gap: 30px;
        }

        .nav-links a {
            color: var(--gray);
            text-decoration: none;
            font-weight: 500;
            font-size: 1.1rem;
            transition: var(--transition);
            position: relative;
        }

        .nav-links a:hover, .nav-links a.active {
            color: var(--light);
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: var(--secondary);
            transition: var(--transition);
        }

        .nav-links a:hover::after, .nav-links a.active::after {
            width: 100%;
        }

        .mobile-toggle {
            display: none;
            font-size: 1.5rem;
            cursor: pointer;
        }

        /* Page Sections */
        .page {
            min-height: 100vh;
            padding-top: 100px;
            padding-bottom: 80px;
        }

        .section-title {
            font-size: 2.5rem;
            margin-bottom: 50px;
            position: relative;
            display: inline-block;
        }

        .section-title::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 0;
            width: 60px;
            height: 4px;
            background: var(--secondary);
            border-radius: 2px;
        }

        /* Home Section */
        #home {
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            position: relative;
        }

        .hero-content {
            max-width: 800px;
            z-index: 2;
        }

        .hero-title {
            font-size: 4rem;
            font-weight: 800;
            margin-bottom: 20px;
            line-height: 1.2;
        }

        .hero-title span {
            color: var(--secondary);
            display: block;
        }

        .hero-subtitle {
            font-size: 1.5rem;
            color: var(--gray);
            margin-bottom: 30px;
        }

        .cta-button {
            display: inline-block;
            background: var(--primary);
            color: white;
            padding: 14px 40px;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            font-size: 1.1rem;
            transition: var(--transition);
            border: 2px solid var(--primary);
            margin: 10px;
        }

        .cta-button:hover {
            background: transparent;
            transform: translateY(-3px);
            box-shadow: var(--shadow);
        }

        .cta-button.secondary {
            background: transparent;
            border-color: var(--secondary);
        }

        .cta-button.secondary:hover {
            background: var(--secondary);
        }

        /* About Section */
        .about-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
            align-items: center;
        }

        .about-image {
            border-radius: var(--border-radius);
            overflow: hidden;
            box-shadow: var(--shadow);
            position: relative;
        }

        .about-image::before {
            content: '';
            position: absolute;
            top: -20px;
            left: -20px;
            width: 100%;
            height: 100%;
            border: 3px solid var(--secondary);
            border-radius: var(--border-radius);
            z-index: -1;
        }

        .about-image img {
            width: 100%;
            display: block;
            border-radius: var(--border-radius);
        }

        .about-text h3 {
            font-size: 1.8rem;
            margin-bottom: 20px;
            color: var(--secondary);
        }

        .about-text p {
            margin-bottom: 20px;
            color: var(--gray);
        }

        .skills {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin-top: 30px;
        }

        .skill {
            background: rgba(37, 99, 235, 0.1);
            padding: 8px 20px;
            border-radius: 50px;
            font-size: 0.9rem;
            border: 1px solid rgba(37, 99, 235, 0.3);
        }

        /* Education Section */
        .timeline {
            position: relative;
            max-width: 800px;
            margin: 0 auto;
        }

        .timeline::before {
            content: '';
            position: absolute;
            top: 0;
            bottom: 0;
            width: 4px;
            background: var(--secondary);
            left: 50%;
            margin-left: -2px;
        }

        .timeline-item {
            position: relative;
            margin-bottom: 50px;
            width: 50%;
            padding: 20px;
            background: rgba(30, 41, 59, 0.7);
            border-radius: var(--border-radius);
            box-shadow: var(--shadow);
        }

        .timeline-item:nth-child(odd) {
            left: 0;
            text-align: right;
        }

        .timeline-item:nth-child(even) {
            left: 50%;
        }

        .timeline-item::after {
            content: '';
            position: absolute;
            width: 20px;
            height: 20px;
            background: var(--secondary);
            border-radius: 50%;
            top: 30px;
        }

        .timeline-item:nth-child(odd)::after {
            right: -10px;
        }

        .timeline-item:nth-child(even)::after {
            left: -10px;
        }

        .timeline-year {
            color: var(--secondary);
            font-weight: 600;
            margin-bottom: 10px;
        }

        .timeline-title {
            font-size: 1.4rem;
            margin-bottom: 10px;
        }

        .timeline-subtitle {
            color: var(--gray);
            font-style: italic;
        }

        /* Projects Section */
        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 30px;
        }

        .project-card {
            background: rgba(30, 41, 59, 0.7);
            border-radius: var(--border-radius);
            overflow: hidden;
            box-shadow: var(--shadow);
            transition: var(--transition);
        }

        .project-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
        }

        .project-image {
            height: 200px;
            overflow: hidden;
        }

        .project-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: var(--transition);
        }

        .project-card:hover .project-image img {
            transform: scale(1.1);
        }

        .project-content {
            padding: 25px;
        }

        .project-title {
            font-size: 1.4rem;
            margin-bottom: 15px;
        }

        .project-description {
            color: var(--gray);
            margin-bottom: 20px;
        }

        .project-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 20px;
        }

        .project-tag {
            background: rgba(14, 165, 233, 0.1);
            color: var(--secondary);
            padding: 5px 12px;
            border-radius: 50px;
            font-size: 0.8rem;
        }

        .project-link {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            color: var(--secondary);
            text-decoration: none;
            font-weight: 600;
            transition: var(--transition);
        }

        .project-link:hover {
            gap: 12px;
        }

        /* Contact Section */
        .contact-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
        }

        .contact-info {
            display: flex;
            flex-direction: column;
            gap: 30px;
        }

        .contact-item {
            display: flex;
            gap: 20px;
            align-items: flex-start;
        }

        .contact-icon {
            background: rgba(14, 165, 233, 0.1);
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            color: var(--secondary);
            flex-shrink: 0;
        }

        .contact-text h3 {
            margin-bottom: 8px;
            font-size: 1.3rem;
        }

        .contact-text p {
            color: var(--gray);
        }

        .social-links {
            display: flex;
            gap: 20px;
            margin-top: 30px;
        }

        .social-link {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 45px;
            height: 45px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.05);
            color: var(--light);
            font-size: 1.2rem;
            transition: var(--transition);
        }

        .social-link:hover {
            background: var(--secondary);
            transform: translateY(-5px);
        }

        .contact-form {
            background: rgba(30, 41, 59, 0.7);
            padding: 40px;
            border-radius: var(--border-radius);
            box-shadow: var(--shadow);
        }

        .form-group {
            margin-bottom: 25px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 500;
        }

        .form-control {
            width: 100%;
            padding: 14px;
            background: rgba(15, 23, 42, 0.5);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            color: var(--light);
            font-size: 1rem;
            transition: var(--transition);
        }

        .form-control:focus {
            outline: none;
            border-color: var(--secondary);
            background: rgba(15, 23, 42, 0.7);
        }

        textarea.form-control {
            min-height: 150px;
            resize: vertical;
        }

        .submit-btn {
            background: var(--primary);
            color: white;
            border: none;
            padding: 14px 40px;
            border-radius: 50px;
            font-weight: 600;
            font-size: 1.1rem;
            cursor: pointer;
            transition: var(--transition);
            width: 100%;
        }

        .submit-btn:hover {
            background: #1d4ed8;
            transform: translateY(-3px);
        }

        /* Footer */
        footer {
            background: rgba(15, 23, 42, 0.9);
            padding: 30px 0;
            text-align: center;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
        }

        .footer-content {
            color: var(--gray);
            font-size: 0.9rem;
        }

        /* Responsive Design */
        @media (max-width: 992px) {
            .hero-title {
                font-size: 3.2rem;
            }
            
            .about-content,
            .contact-container {
                grid-template-columns: 1fr;
            }
            
            .timeline::before {
                left: 30px;
            }
            
            .timeline-item {
                width: 100%;
                padding-left: 70px;
                padding-right: 25px;
                left: 0 !important;
                text-align: left !important;
            }
            
            .timeline-item:nth-child(odd)::after,
            .timeline-item:nth-child(even)::after {
                left: 20px;
            }
        }

        @media (max-width: 768px) {
            .nav-links {
                position: fixed;
                top: 80px;
                left: 0;
                right: 0;
                background: rgba(30, 41, 59, 0.95);
                flex-direction: column;
                align-items: center;
                padding: 30px 0;
                gap: 25px;
                clip-path: circle(0px at top right);
                transition: clip-path 0.4s ease;
            }
            
            .nav-links.active {
                clip-path: circle(1000px at top right);
            }
            
            .mobile-toggle {
                display: block;
            }
            
            .hero-title {
                font-size: 2.5rem;
            }
            
            .projects-grid {
                grid-template-columns: 1fr;
            }
        }

        @media (max-width: 480px) {
            .hero-title {
                font-size: 2rem;
            }
            
            .section-title {
                font-size: 2rem;
            }
            
            .cta-button {
                display: block;
                margin: 10px auto;
            }
        }
    </style>
</head>
<body>
    <nav>
        <div class="container nav-container">
            <a href="/" class="logo">
                <i class="fas fa-code"></i>MD<span>SAIF</span>
            </a>
            <div class="nav-links">
                <a href="/">Home</a>
                <a href="/about">About</a>
                <a href="/education">Education</a>
                <a href="/projects" class="active">Projects</a>
                <a href="/contact">Contact</a>
            </div>
            <div class="mobile-toggle">
                <i class="fas fa-bars"></i>
            </div>
        </div>
    </nav>

    <section id="projects" class="page">
        <div class="container">
            <h2 class="section-title">My Projects</h2>
            <div class="projects-grid">
                <div class="project-card">
                    <div class="project-content">
                        <h3 class="project-title">FILE SHARING WEB SITE</h3>
                        <p class="project-description">Peer-to-peer file sharing with end-to-end encryption. Built with Python Flask. No server storage, no waiting.</p>
                        <div class="project-tags">
                            <span class="project-tag">HTML,CSS</span>
                            <span class="project-tag">JAVASCRIPT</span>
                            <span class="project-tag">PYTHON</span>
                        </div>
                        <a href="https://file-share-web-server-io.onrender.com/" class="project-link">View Project <i class="fas fa-arrow-right"></i></a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const mobileToggle = document.querySelector('.mobile-toggle');
            const navMenu = document.querySelector('.nav-links');
            
            mobileToggle.addEventListener('click', function() {
                navMenu.classList.toggle('active');
            });
            
            document.addEventListener('click', function(e) {
                if (!e.target.closest('.nav-container') && navMenu.classList.contains('active')) {
                    navMenu.classList.remove('active');
                }
            });
        });
    </script>
</body>
</html>
        ''',

        "contact": '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary: #2563eb;
            --secondary: #0ea5e9;
            --dark: #1e293b;
            --light: #f8fafc;
            --gray: #94a3b8;
            --accent: #f97316;
            --transition: all 0.3s ease;
            --shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
            --border-radius: 12px;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0f172a, #1e293b);
            color: var(--light);
            line-height: 1.6;
            overflow-x: hidden;
            min-height: 100vh;
        }

        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* Navigation */
        nav {
            position: fixed;
            top: 0;
            width: 100%;
            background: rgba(30, 41, 59, 0.95);
            backdrop-filter: blur(10px);
            z-index: 1000;
            box-shadow: var(--shadow);
        }

        .nav-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 0;
        }

        .logo {
            font-weight: 800;
            font-size: 1.8rem;
            color: var(--light);
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .logo span {
            color: var(--secondary);
        }

        .nav-links {
            display: flex;
            gap: 30px;
        }

        .nav-links a {
            color: var(--gray);
            text-decoration: none;
            font-weight: 500;
            font-size: 1.1rem;
            transition: var(--transition);
            position: relative;
        }

        .nav-links a:hover, .nav-links a.active {
            color: var(--light);
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: var(--secondary);
            transition: var(--transition);
        }

        .nav-links a:hover::after, .nav-links a.active::after {
            width: 100%;
        }

        .mobile-toggle {
            display: none;
            font-size: 1.5rem;
            cursor: pointer;
        }

        /* Page Sections */
        .page {
            min-height: 100vh;
            padding-top: 100px;
            padding-bottom: 80px;
        }

        .section-title {
            font-size: 2.5rem;
            margin-bottom: 50px;
            position: relative;
            display: inline-block;
        }

        .section-title::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 0;
            width: 60px;
            height: 4px;
            background: var(--secondary);
            border-radius: 2px;
        }

        /* Home Section */
        #home {
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            position: relative;
        }

        .hero-content {
            max-width: 800px;
            z-index: 2;
        }

        .hero-title {
            font-size: 4rem;
            font-weight: 800;
            margin-bottom: 20px;
            line-height: 1.2;
        }

        .hero-title span {
            color: var(--secondary);
            display: block;
        }

        .hero-subtitle {
            font-size: 1.5rem;
            color: var(--gray);
            margin-bottom: 30px;
        }

        .cta-button {
            display: inline-block;
            background: var(--primary);
            color: white;
            padding: 14px 40px;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            font-size: 1.1rem;
            transition: var(--transition);
            border: 2px solid var(--primary);
            margin: 10px;
        }

        .cta-button:hover {
            background: transparent;
            transform: translateY(-3px);
            box-shadow: var(--shadow);
        }

        .cta-button.secondary {
            background: transparent;
            border-color: var(--secondary);
        }

        .cta-button.secondary:hover {
            background: var(--secondary);
        }

        /* About Section */
        .about-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
            align-items: center;
        }

        .about-image {
            border-radius: var(--border-radius);
            overflow: hidden;
            box-shadow: var(--shadow);
            position: relative;
        }

        .about-image::before {
            content: '';
            position: absolute;
            top: -20px;
            left: -20px;
            width: 100%;
            height: 100%;
            border: 3px solid var(--secondary);
            border-radius: var(--border-radius);
            z-index: -1;
        }

        .about-image img {
            width: 100%;
            display: block;
            border-radius: var(--border-radius);
        }

        .about-text h3 {
            font-size: 1.8rem;
            margin-bottom: 20px;
            color: var(--secondary);
        }

        .about-text p {
            margin-bottom: 20px;
            color: var(--gray);
        }

        .skills {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin-top: 30px;
        }

        .skill {
            background: rgba(37, 99, 235, 0.1);
            padding: 8px 20px;
            border-radius: 50px;
            font-size: 0.9rem;
            border: 1px solid rgba(37, 99, 235, 0.3);
        }

        /* Education Section */
        .timeline {
            position: relative;
            max-width: 800px;
            margin: 0 auto;
        }

        .timeline::before {
            content: '';
            position: absolute;
            top: 0;
            bottom: 0;
            width: 4px;
            background: var(--secondary);
            left: 50%;
            margin-left: -2px;
        }

        .timeline-item {
            position: relative;
            margin-bottom: 50px;
            width: 50%;
            padding: 20px;
            background: rgba(30, 41, 59, 0.7);
            border-radius: var(--border-radius);
            box-shadow: var(--shadow);
        }

        .timeline-item:nth-child(odd) {
            left: 0;
            text-align: right;
        }

        .timeline-item:nth-child(even) {
            left: 50%;
        }

        .timeline-item::after {
            content: '';
            position: absolute;
            width: 20px;
            height: 20px;
            background: var(--secondary);
            border-radius: 50%;
            top: 30px;
        }

        .timeline-item:nth-child(odd)::after {
            right: -10px;
        }

        .timeline-item:nth-child(even)::after {
            left: -10px;
        }

        .timeline-year {
            color: var(--secondary);
            font-weight: 600;
            margin-bottom: 10px;
        }

        .timeline-title {
            font-size: 1.4rem;
            margin-bottom: 10px;
        }

        .timeline-subtitle {
            color: var(--gray);
            font-style: italic;
        }

        /* Projects Section */
        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 30px;
        }

        .project-card {
            background: rgba(30, 41, 59, 0.7);
            border-radius: var(--border-radius);
            overflow: hidden;
            box-shadow: var(--shadow);
            transition: var(--transition);
        }

        .project-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
        }

        .project-image {
            height: 200px;
            overflow: hidden;
        }

        .project-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: var(--transition);
        }

        .project-card:hover .project-image img {
            transform: scale(1.1);
        }

        .project-content {
            padding: 25px;
        }

        .project-title {
            font-size: 1.4rem;
            margin-bottom: 15px;
        }

        .project-description {
            color: var(--gray);
            margin-bottom: 20px;
        }

        .project-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 20px;
        }

        .project-tag {
            background: rgba(14, 165, 233, 0.1);
            color: var(--secondary);
            padding: 5px 12px;
            border-radius: 50px;
            font-size: 0.8rem;
        }

        .project-link {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            color: var(--secondary);
            text-decoration: none;
            font-weight: 600;
            transition: var(--transition);
        }

        .project-link:hover {
            gap: 12px;
        }

        /* Contact Section */
        .contact-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
        }

        .contact-info {
            display: flex;
            flex-direction: column;
            gap: 30px;
        }

        .contact-item {
            display: flex;
            gap: 20px;
            align-items: flex-start;
        }

        .contact-icon {
            background: rgba(14, 165, 233, 0.1);
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            color: var(--secondary);
            flex-shrink: 0;
        }

        .contact-text h3 {
            margin-bottom: 8px;
            font-size: 1.3rem;
        }

        .contact-text p {
            color: var(--gray);
        }

        .social-links {
            display: flex;
            gap: 20px;
            margin-top: 30px;
        }

        .social-link {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 45px;
            height: 45px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.05);
            color: var(--light);
            font-size: 1.2rem;
            transition: var(--transition);
        }

        .social-link:hover {
            background: var(--secondary);
            transform: translateY(-5px);
        }

        .contact-form {
            background: rgba(30, 41, 59, 0.7);
            padding: 40px;
            border-radius: var(--border-radius);
            box-shadow: var(--shadow);
        }

        .form-group {
            margin-bottom: 25px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 500;
        }

        .form-control {
            width: 100%;
            padding: 14px;
            background: rgba(15, 23, 42, 0.5);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            color: var(--light);
            font-size: 1rem;
            transition: var(--transition);
        }

        .form-control:focus {
            outline: none;
            border-color: var(--secondary);
            background: rgba(15, 23, 42, 0.7);
        }

        textarea.form-control {
            min-height: 150px;
            resize: vertical;
        }

        .submit-btn {
            background: var(--primary);
            color: white;
            border: none;
            padding: 14px 40px;
            border-radius: 50px;
            font-weight: 600;
            font-size: 1.1rem;
            cursor: pointer;
            transition: var(--transition);
            width: 100%;
        }

        .submit-btn:hover {
            background: #1d4ed8;
            transform: translateY(-3px);
        }

        /* Footer */
        footer {
            background: rgba(15, 23, 42, 0.9);
            padding: 30px 0;
            text-align: center;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
        }

        .footer-content {
            color: var(--gray);
            font-size: 0.9rem;
        }

        /* Responsive Design */
        @media (max-width: 992px) {
            .hero-title {
                font-size: 3.2rem;
            }
            
            .about-content,
            .contact-container {
                grid-template-columns: 1fr;
            }
            
            .timeline::before {
                left: 30px;
            }
            
            .timeline-item {
                width: 100%;
                padding-left: 70px;
                padding-right: 25px;
                left: 0 !important;
                text-align: left !important;
            }
            
            .timeline-item:nth-child(odd)::after,
            .timeline-item:nth-child(even)::after {
                left: 20px;
            }
        }

        @media (max-width: 768px) {
            .nav-links {
                position: fixed;
                top: 80px;
                left: 0;
                right: 0;
                background: rgba(30, 41, 59, 0.95);
                flex-direction: column;
                align-items: center;
                padding: 30px 0;
                gap: 25px;
                clip-path: circle(0px at top right);
                transition: clip-path 0.4s ease;
            }
            
            .nav-links.active {
                clip-path: circle(1000px at top right);
            }
            
            .mobile-toggle {
                display: block;
            }
            
            .hero-title {
                font-size: 2.5rem;
            }
            
            .projects-grid {
                grid-template-columns: 1fr;
            }
        }

        @media (max-width: 480px) {
            .hero-title {
                font-size: 2rem;
            }
            
            .section-title {
                font-size: 2rem;
            }
            
            .cta-button {
                display: block;
                margin: 10px auto;
            }
        }
    </style>
</head>
<body>
    <nav>
        <div class="container nav-container">
            <a href="/" class="logo">
                <i class="fas fa-code"></i>MD<span>SAIF</span>
            </a>
            <div class="nav-links">
                <a href="/">Home</a>
                <a href="/about">About</a>
                <a href="/education">Education</a>
                <a href="/projects">Projects</a>
                <a href="/contact" class="active">Contact</a>
            </div>
            <div class="mobile-toggle">
                <i class="fas fa-bars"></i>
            </div>
        </div>
    </nav>

    <section id="contact" class="page">
        <div class="container">
            <h2 class="section-title">Get In Touch</h2>
            <div class="contact-container">
                <div class="contact-info">
                    <div class="contact-item">
                        <div class="contact-icon">
                            <i class="fas fa-map-marker-alt"></i>
                        </div>
                        <div class="contact-text">
                            <h3>Location</h3>
                            <p>Hyderabad, Telangana, South India</p>
                        </div>
                    </div>
                    <div class="contact-item">
                        <div class="contact-icon">
                            <i class="fas fa-envelope"></i>
                        </div>
                        <div class="contact-text">
                            <h3>Email</h3>
                            <p>mohammedsaifms2006@gmail.com</p>
                        </div>
                    </div>
                    <div class="social-links">
                        <a href="https://github.com/MOHAMMEDSAIF-07" class="social-link"><i class="fab fa-github"></i></a>
                        <a href="https://t.me/Mdsaif_0007" class="social-link"><i class="fab fa-telegram"></i></a>
                        <a href="https://www.instagram.com/md.saif____" class="social-link"><i class="fab fa-instagram"></i></a>
                        <a href="https://www.linkedin.com/in/mohammed-saif-hyderabad" class="social-link"><i class="fab fa-linkedin"></i></a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const mobileToggle = document.querySelector('.mobile-toggle');
            const navMenu = document.querySelector('.nav-links');
            
            mobileToggle.addEventListener('click', function() {
                navMenu.classList.toggle('active');
            });
            
            document.addEventListener('click', function(e) {
                if (!e.target.closest('.nav-container') && navMenu.classList.contains('active')) {
                    navMenu.classList.remove('active');
                }
            });
        });
    </script>
</body>
</html>
        '''
}
    return pages.get(page_name, "")

@app.route('/')
def index():
    return Response(get_page("index"), mimetype='text/html')

@app.route('/about')
def about():
    return Response(get_page("about"), mimetype='text/html')

@app.route('/education')
def education():
    return Response(get_page("education"), mimetype='text/html')

@app.route('/projects')
def projects():
    return Response(get_page("projects"), mimetype='text/html')

@app.route('/contact')
def contact():
    return Response(get_page("contact"), mimetype='text/html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
