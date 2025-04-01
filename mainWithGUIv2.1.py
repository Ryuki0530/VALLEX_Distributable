import tkinter as tk
from tkinter import filedialog, messagebox
from scipy.io.wavfile import write as write_wav
from playsound import playsound
import pathlib
import torch.serialization
import os
from datetime import datetime

# WindowsPath 対応
torch.serialization.add_safe_globals({pathlib.WindowsPath: "WindowsPath"})

# VALL-EX モジュール読み込み
from utils.prompt_making import make_prompt
from utils.generation import SAMPLE_RATE, generate_audio, preload_models

# モデル事前読み込み
preload_models()

# 出力先ディレクトリを固定
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate():
    model_name = "UserModel"
    sample_voice = sample_voice_path.get()
    sample_transcript = transcript_entry.get("1.0", tk.END).strip()
    text_prompt = text_entry.get("1.0", tk.END).strip()
    use_existing_prompt = use_existing_var.get()

    if not text_prompt:
        messagebox.showerror("エラー", "合成する文章は必須です。")
        return

    try:
        if not use_existing_prompt:
            if not sample_voice or not sample_transcript:
                messagebox.showerror("エラー", "プロンプト作成には音声とスクリプトが必要です。")
                return
            make_prompt(name=model_name, audio_prompt_path=sample_voice, transcript=sample_transcript)

        # 現在時刻でファイル名を生成
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        save_file = os.path.join(OUTPUT_DIR, f"{timestamp}.wav")

        audio_array = generate_audio(text_prompt, language="ja", prompt=model_name)
        write_wav(save_file, SAMPLE_RATE, audio_array)

        playsound(save_file)  # 成功時は再生のみ、メッセージ表示なし

    except Exception as e:
        messagebox.showerror("エラー", f"合成中にエラーが発生しました:\n{str(e)}")

def browse_file(entry):
    filepath = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
    if filepath:
        entry.delete(0, tk.END)
        entry.insert(0, filepath)

# GUIウィンドウ作成
root = tk.Tk()
root.title("VALL-EX 音声合成GUI")
root.iconbitmap(default = "icon.ico")

use_existing_var = tk.BooleanVar()
tk.Checkbutton(root, text="既存プロンプトを使用（UserModel）", variable=use_existing_var).grid(row=0, column=1, columnspan=2, sticky="w")

tk.Label(root, text="サンプル音声:").grid(row=1, column=0, sticky="e")
sample_voice_path = tk.Entry(root, width=30)
sample_voice_path.grid(row=1, column=1)
tk.Button(root, text="参照", command=lambda: browse_file(sample_voice_path)).grid(row=1, column=2)

tk.Label(root, text="サンプル文字列:").grid(row=2, column=0, sticky="ne")
transcript_entry = tk.Text(root, height=2, width=30)
transcript_entry.grid(row=2, column=1, columnspan=2)

tk.Label(root, text="合成したい文章:").grid(row=3, column=0, sticky="ne")
text_entry = tk.Text(root, height=2, width=30)
text_entry.grid(row=3, column=1, columnspan=2)

tk.Button(root, text="音声合成＆再生", command=generate).grid(row=4, column=1, pady=10)

root.mainloop()
