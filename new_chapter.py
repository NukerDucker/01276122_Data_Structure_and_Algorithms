import os

def main():
    chapter = input("Enter chapter number: ").strip()
    folder_name = f"CH{chapter}"
    os.makedirs(folder_name, exist_ok=True)
    for i in range(1, 6):
        file_name = f"ex{i:02}.py"
        file_path = os.path.join(folder_name, file_name)
    
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(f"# {file_name} for Chapter {chapter}\n")
            print(f"Created {file_path}")
        else:
            print(f"Skipped {file_path} (already exists)")
    
    print("Done!")

if __name__ == "__main__":
    main()
