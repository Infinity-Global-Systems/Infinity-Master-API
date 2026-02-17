import os, subprocess

def build_sovereign_tool(script_name):
    print(f"--- [IGS-BUILD] ASSEMBLING: {script_name} ---")
    dist_path = r'D:\IGS_GLOBAL_SYSTEMS\Production'
    work_path = r'D:\IGS_GLOBAL_SYSTEMS\Production\Temp'
    
    # تحويل السكربت إلى ملف EXE صامت ومشفر
    cmd = [
        'pyinstaller',
        '--onefile',
        '--windowed',
        '--distpath', dist_path,
        '--workpath', work_path,
        '--name', 'IGS_Core_Tool',
        script_name
    ]
    
    subprocess.run(cmd)
    print(f"\n[!] BUILD COMPLETE: Check {dist_path}")

if __name__ == "__main__":
    # بناء مركز القيادة الرئيسي كمنتج نهائي
    target = r'D:\IGS_GLOBAL_SYSTEMS\Command Center\IGS_Main_Controller.py'
    build_sovereign_tool(target)
