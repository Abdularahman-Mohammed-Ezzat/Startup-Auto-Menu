<!DOCTYPE html>
<html lang="en">
<body>
    <h1>Startup Auto Menu</h1>
    <p>Startup Auto Menu is a Python application designed for Linux environments that enhances your productivity by presenting a beautiful GUI at system startup. This menu allows you to choose a task category, such as "Writing," "Programming," or "Browsing," and then offers a selection of relevant tools to launch. Once a tool is chosen, the app launches it and then exits, streamlining your workflow from the moment your system boots up.</p>
    <h2>Features</h2>
    <ul>
        <li><strong>Task Categories:</strong> Choose from various categories like Writing, Programming, Browsing, Editing, Reading, Taking Notes, and Learning.</li>
        <li><strong>Tool Selection:</strong> Each category presents a curated list of tools tailored to the task at hand.</li>
        <li><strong>Seamless Startup:</strong> Automatically runs at system startup, making it easy to dive right into your tasks.</li>
        <li><strong>Customizable:</strong> Easily add or modify task categories and associated tools to suit your workflow.</li>
    </ul>
    <h2>Installation</h2>
    <ol>
      
  <li><strong>Clone the Repository:</strong>
    
    git clone https://github.com/yourusername/startup-auto-menu.git
    cd startup-auto-menu
            
</li>
        <li><strong>Install Dependencies:</strong>
            <p>Ensure you have Python and pip installed. Then, install the required Python libraries:</p>
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li><strong>Set Up Auto Start:</strong>
            <p>Create a <code>.desktop</code> entry in your autostart directory to run the app at startup. Here's a sample:</p>
          
    [Desktop Entry]
    Type=Application
    Exec=/path/to/startup-auto-menu/startup_auto_menu.py
    Hidden=false
    NoDisplay=false
    X-GNOME-Autostart-enabled=true
    Name=Startup Auto Menu
    Comment=Launch Startup Auto Menu at system startup


  </li>
        <li><strong>Run the Application:</strong>
            <p>You can manually run the application using:</p>
        
      
    python3 startup_auto_menu.py

  </li>
    </ol>

  <h2>Usage</h2>
  <ol>
      <li>Upon system startup, the Startup Auto Menu will appear.</li>
      <li>Select a task category (e.g., "Programming").</li>
      <li>Choose from the list of tools (e.g., "VSCode + GPT").</li>
      <li>The selected tool will launch, and the menu will close.</li>
  </ol>

  <h2>Customization</h2>
  <p>To add or modify task categories and tools:</p>
  <ol>
      <li>Edit the <code>menu_configurations.json</code> file in the project directory.</li>
      <li>Follow the JSON structure to add new categories or tools.</li>
  </ol>
  <p>Example:</p>
  
    {
        "categories": [
          {
            "name": "Writing",
            "tools": [
              {"name": "LibreOffice Writer", "command": "libreoffice --writer"},
              {"name": "FocusWriter", "command": "focuswriter"}
            ]
          }
        ]
      }

<h2>Contributing</h2>
    <p>Contributions are welcome! If you have ideas for new features, improvements, or bug fixes, feel free to fork the repository and submit a pull request.</p>

  <h2>License</h2>
  <p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for more details.</p>

  <h2>Contact</h2>
  <p>If you have any questions or need further assistance, feel free to reach out:</p>
  <ul>
      <li><strong>Author:</strong> Abd El-Rahman Mohammed Ezzat</li>
      <li><strong>Email:</strong> <a href="mailto:abdo.ezzat.ahmed@gmail.com">abdo.ezzat.ahmed@gmail.com</a></li>
      <li><strong>GitHub:</strong> <a href="https://github.com/Abdularahman-Mohammed-Ezzat">Abdularahman-Mohammed-Ezzat</a></li>
  </ul>
</body>
</html>
