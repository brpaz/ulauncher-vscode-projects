# Ulauncher VS Code Git Projects

[![Ulauncher Extension](https://img.shields.io/badge/Ulauncher-Extension-green.svg?style=for-the-badge)](https://ext.ulauncher.io/-/github-brpaz-ulauncher-vscode-projects)
[![CircleCI](https://img.shields.io/circleci/build/github/brpaz/ulauncher-vscode-projects.svg?style=for-the-badge)](https://circleci.com/gh/brpaz/ulauncher-vscode-projects)
![License](https://img.shields.io/github/license/brpaz/ulauncher-vscode-projects.svg?style=for-the-badge)

> [Ulauncher](https://ulauncher.io) extension that allows you to open projects managed by [VSCode Project Manager](https://github.com/alefragnani/vscode-project-manager) Extension.

## Demo

![demo](demo.gif)

## Requirements

- Ulauncher 5
- Python 3
- Visual Studio Code with [Project Manager](https://github.com/alefragnani/vscode-project-manager) extension installed.

## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```
https://github.com/brpaz/ulauncher-vscode-projects
```

## Usage

- Type `projects` into ulauncher input to see a list your VS Code projects. (only git based projects are supported for now.).
- "Enter" will open the project in VS Code while "ALT + Enter" will open in the default file manager.

If you save the message saying "No project found" make sure you the the VS Code Extension correctly installed. You might need to refresh your projects list
so the cache file read by this extension will be created. "F1 -> Project Manager: Referesh Projects".

## Development

```
git clone https://github.com/brpaz/vscode-projects
make link
```

The `make link` command will symlink the cloned repo into the appropriate location on the ulauncher extensions folder.

To see your changes, stop ulauncher and run it from the command line with: `ulauncher -v`.

## Contributing

Contributions, issues and Features requests are welcome.

## Show your support

<a href="https://www.buymeacoffee.com/Z1Bu6asGV" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

## License 

Copywright @ 2019 [Bruno Paz](https://github.com/brpaz)

This project is [MIT](LLICENSE) Licensed.
