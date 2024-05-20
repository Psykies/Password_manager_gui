# Password_manager_gui

Here's a GitHub README file explaining the functionality of your code:

```markdown
# Password Manager

This is a simple password manager application built using Python's Tkinter library. It allows users to generate secure passwords, save them along with website and email information, and search for previously saved passwords.

## Functionality

### Create Password
- Generates a random password containing a combination of letters (uppercase and lowercase), symbols, and numbers.
- The length of the password is randomly chosen between 9 and 16 characters.

### Save Password
- Saves the website, email, and password information into a JSON file named `data.json`.
- Checks for empty fields and displays an error message if any field is left empty.
- If the `data.json` file doesn't exist, it creates one and saves the new data.
- If the file exists but is empty or doesn't contain any valid JSON data, it writes the new data into the file.
- If the file and data both exist, it updates the existing data with the new one.

### Search
- Searches for the email and password associated with a particular website.
- Displays the search result in a messagebox if the website data is found in the JSON file.
- If the file is missing or empty, it displays an error message.

## UI Design
- The UI consists of labels, entry fields, and buttons created using Tkinter.
- Users can input website, email, and password information.
- The logo of the application is displayed at the top.
- Buttons for search, password generation, and saving passwords are provided.

## Dependencies
- Python 3.x
- Tkinter library

## How to Use
1. Run the Python script `password_manager.py`.
2. Input website, email, and password information.
3. Click on "Generate Password" to create a random password.
4. Click on "Add" to save the entered information.
5. Use the "Search" button to find saved passwords for specific websites.

## Examples
![Screenshot 2024-05-20 131419](https://github.com/Psykies/Password_manager_gui/assets/32191652/5d41e25b-6f8d-4615-802e-9600ccd00fb6)
![Screenshot 2024-05-20 131205](https://github.com/Psykies/Password_manager_gui/assets/32191652/8395952e-c3d0-4645-981c-7450da4735f0)
![Screenshot 2024-05-20 131124](https://github.com/Psykies/Password_manager_gui/assets/32191652/13a6dcd0-c0e7-446f-939b-6d9a0a8f5651)


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
