import streamlit as st
import base64
import pandas as pd
import numpy as np



def set_video_background(video_path):
    try:
        with open(video_path, "rb") as f:
            video_data = f.read()
        video_base64 = base64.b64encode(video_data).decode("utf-8")

        st.markdown(
            f"""
            <style>
            /* Основные стили приложения */
            .stApp {{
                background-color: transparent;
            }}

            /* Контейнер для видео */
            #video-container {{
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                z-index: -1;
                overflow: hidden;
            }}

            /* Стили самого видео */
            #bg-video {{
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                min-width: 80%;
                min-height: 80%;
                object-fit: cover;
            }}

            /* Затемнение для лучшей читаемости */
            #video-overlay {{
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-color: rgba(0,0,0,0.3);
                z-index: -1;
            }}

            /* Стили для контента */
            .content {{
                position: relative;
                z-index: 1;
                color: white;
                padding: 20px;
            }}

            /* Стили для красивого заголовка */
            .fancy-title {{
                font-family: 'Arial', sans-serif;
                font-size: 4rem;
                font-weight: 700;
                text-align: center;
                margin: 2rem 0;
                color: #fff;
                text-shadow: 0 0 10px rgba(255,255,255,0.5);
                position: relative;
                animation: glow 2s ease-in-out infinite alternate;
            }}

            .fancy-title::after {{
                content: '';
                display: block;
                width: 100px;
                height: 4px;
                background: linear-gradient(90deg, transparent, #fff, transparent);
                margin: 10px auto;
            }}

            @keyframes glow {{
                from {{
                    text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 15px #e60073, 0 0 20px #e60073;
                }}
                to {{
                    text-shadow: 0 0 10px #fff, 0 0 20px #ff4da6, 0 0 30px #ff4da6, 0 0 40px #ff4da6;
                }}
            }}

            /* Стили для красивого текста */
            .fancy-text {{
                font-family: 'Georgia', serif;
                font-size: 1.5rem;
                line-height: 1.6;
                text-align: center;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background-color: rgba(0,0,0,0.5);
                border-radius: 15px;
                box-shadow: 0 0 20px rgba(255,255,255,0.2);
                backdrop-filter: blur(5px);
            }}
            </style>

            <!-- HTML-разметка для видео -->
            <div id="video-container">
                <video id="bg-video" autoplay muted loop playsinline>
                    <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
                </video>
                <div id="video-overlay"></div>
            </div>
            """,
            unsafe_allow_html=True
        )
    except Exception as e:
        st.error(f"Ошибка загрузки видео: {e}")




