#file handling, The open() function takes two parameters; filename, and mode.
#There are four different methods (modes) for opening a file: 
'''
 "r" - Read - Default value. Opens a file for reading, error if the file does not exist 
#"a" - Append - Opens a file for appending, creates the file if it does not exist 
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists */

#In addition you can specify if the file should be handled as binary or text mode
'''
'''
This is a multiline
comment.
'''

#python sectools.py secimage -s -c D:\Project\R2ex\Software_build\Unpacking_tool_Splash_Screen\Unpacking_tool_Splash_Screen\common\sectools\config/nicobar/nicobar_secimage.xml --cfg_selected_cert_config=oem_certs -i D:\Project\R2ex\Signing_software_images\Unsigned\xbl.elf -o D:\Project\R2ex\Signing_software_images -v

#input("Press Enter to continue...")
while True:
    try:
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break

from pathlib import Path

'''
def copy_and_rename_pathlib(src_path, dest_path, new_name):
    # Create Path objects
    src_path = Path(src_path)
    dest_path = Path(dest_path)

    # Copy and rename the file
    new_path = dest_path / new_name
    src_path.rename(new_path)

# Example usage
source_file = "example.txt"
destination_folder = "destination_folder"
new_file_name = "renamed_example.txt"

copy_and_rename_pathlib(source_file, destination_folder, new_file_name)
print("Successfully Created File and Rename")
'''
