Title: Atom for Markdown editing
Date: 13:02 25th Jan 2017
Modified: 13:02 25th Jan 2017
Category: Tools
Tags: Technical, Tool, Markdown, Atom Introduction
Slug: atom_for_markdown_editing Authors: Zean Qin
Summary: My setup of Atom for Markdown editing.
Below is the Atom setup I have been using for Markdown editing.

Markdown support
----------------

Atom has a variety of community generated packages that can be installed to provide additional functionality. Here are the ones I recommend:

1.	[markdown-writer](https://atom.io/packages/markdown-writer): Adds a bunch of keyboard commands for things like text formatting and creating links & images, along with support for popular static site blogging platforms.
2.	[markdown-scroll-sync](https://atom.io/packages/markdown-scroll-sync): Makes the rendered preview scroll in sync with the Markdown view.
3.	[markdown-format](https://atom.io/packages/markdown-format): Makes your Markdown pretty when you save. Things like renumbering lists so they are actually in order (vs. the 1, 2, 3, 5, 5, 5, 8, 9 I always seem to end up with,) and padding cells in GitHub Flavored Markdown tables so they are more readable.
4.	[tool-bar-markdown-writer](https://atom.io/packages/tool-bar-markdown-writer) and [tool-bar](https://atom.io/packages/tool-bar): tool-bar-markdown-writer adds markdown editing buttons. And you will need to first install the tool-bar plugin to make it appear.

Installing packages
-------------------

Once you’ve installed Atom.io, to install these or any other packages, perform the following steps:

1.	From the File menu, select Settings, then Install. Enter the name of the package you wish to install (or part of the name, such as Markdown to see all packages that contain that word.)
2.	Click the Install button beside the package. If you want to read more about the package before installing, click the title of the package and it will open your browser and display more information.

Configuration
-------------

Once installed, you can use the **Packages** tab from **Settings** to disable, enable, or configure packages.

While some packages have their own configuration, you will also want to look at **File**, **Settings**, **Settings** to configure the following settings for Markdown authoring:

-	**Tab length**: If **Soft tabs** is enabled, then you should set this to 4 since Markdown expects either a single tab or 4 spaces when indenting.
-	**Soft wrap, Soft wrap and preferred line length, and Preferred line length**: This causes the editor to wrap lines at the specified line length. Otherwise, paragraphs will scroll off the editor to the right. Makes things much more readable, especially when the preview window is open.

This last one is a matter of preference. Markdown-Writer does its own special thing with the tab key for indention. In the current version, on Windows, it only seems to indent in a list, while I want it to indent everywhere when I hit the tab key. You can override the current Markdown-Writer functionality by doing the following:

1.	**File**, **Settings**, **Keybindings**, then click the link to your **keymap** file at the top of the page.
2.	Add the following new lines to the end of the **keymap.cson** file:

	<code> ‘atom-text-editor[data-grammar~=\’gfm\’]’:</br>‘tab’: ‘editor:indent’ </code>

	This restores normal tab functionality for Markdown editing. **NOTE**: If you’re using something like Markdown-Format, it may convert 4 spaces to tabs automatically when you save.

Tips
----

To toggle the Markdown preview, use ctrl-shift-m.

If you’ve opend Atom to a specific folder, and it’s showing the tree view side bar, you can dismiss it with ctrl-.

Atom.io checks for package updates automatically. If you see a blue box in the lower right-hand corner, that means some packages have been updated. Click on the blue box to install them.

If you’re working in a folder that contains a lot of Markdown files, don’t even try using the tree view. It’s 100x easier to use ctrl-t and then start typing the file name you want to open. This will search through the directory structure for files that match the text you’ve entered, and you can then click the one you want.

If you need to change the indentation for a section of text (for example, a section of source code,) just select it and hit ctrl-[ or ] to change the indent level.
