var app = Application.currentApplication();
 
app.includeStandardAdditions = true;
 
app.displayNotification("Make sure to commit and push", {
    withTitle: "Hey, you haven't pushed to GitHub today.",
    soundName: "Pop"
});
