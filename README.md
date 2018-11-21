# ulauncher-vscode-git-projects

[![Build Status](https://img.shields.io/travis/com/brpaz/vscode-projects.svg)](https://github.com/brpaz/vscode-projects)
[![GitHub license](https://img.shields.io/github/license/brpaz/vscode-projects.svg)](https://github.com/brpaz/vscode-projects/blob/master/LICENSE)

> [Ulauncher](https://ulauncher.io) extension that allows you to open projects managed by [VSCode Project Manager](https://github.com/alefragnani/vscode-project-manager) Extension.

## Demo

![demo](demo.gif)

## Requirements

- Ulauncher
- Python >= 2.7
- Visual Studio Code with [Project Manager](https://github.com/alefragnani/vscode-project-manager)

## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```
https://github.com/brpaz/vscode-projects
```

## Usage

- Just type `projects` into ulauncher input to see a list your VS Code projects. (only git projects are supported for now.).
- "Enter" will open the project in VS Code while "ALT + Enter" will open in the default file manager.

## Development

```
git clone https://github.com/brpaz/vscode-projects
make link
```

The `make link` command will symlink the cloned repo into the appropriate location on the ulauncher extensions folder.

To see your changes, stop ulauncher and run it from the command line with: `ulauncher -v`.

## Contributing

- Fork it!
- Create your feature branch: git checkout -b my-new-feature
- Commit your changes: git commit -am 'Add some feature'
- Push to the branch: git push origin my-new-feature
- Submit a pull request :D

## License

MIT &copy; [Bruno Paz]
