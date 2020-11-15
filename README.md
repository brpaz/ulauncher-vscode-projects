
# Ulauncher VSCode Projects Extension

[![Ulauncher Extension](https://img.shields.io/badge/Ulauncher-Extension-green.svg?style=for-the-badge)](https://ext.ulauncher.io/-/github-brpaz-ulauncher-vscode-projects)
[![CircleCI](https://img.shields.io/circleci/build/github/brpaz/ulauncher-vscode-projects.svg?style=for-the-badge)](https://circleci.com/gh/brpaz/ulauncher-vscode-projects)
![License](https://img.shields.io/github/license/brpaz/ulauncher-vscode-projects.svg?style=for-the-badge)

> [Ulauncher](https://ulauncher.io) extension that allows you to quickly open your VSCode projects, either managed by [VSCode Project Manager](https://github.com/alefragnani/vscode-project-manager) or directly from VSCode "Recent workspaces".

## Demo

![demo](demo.gif)

## Requirements

- Ulauncher 5
- Python 3
- Visual Studio Code
- [Project Manager](https://github.com/alefragnani/vscode-project-manager) extension. If not installed, you can still use this extension but will fall back to "Recent workspaces".

## Install

You must install the following Python packages required by this extension. You can run the following command in the terminal:

```sh
pip install --user memoization==0.3.1
```

In some Operating systems, you might have to run `pip3` instead of `pip`

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```
https://github.com/brpaz/ulauncher-vscode-projects
```

## Usage

Type `vsp` into ulauncher input, to trigger this extension. You can optionally keep typing to filter the projects list.

[Project Manager](https://github.com/alefragnani/vscode-project-manager) managed projects will appear with the "briefcase" icon, while "Recent workspaces" will have a dark VSCode icon.

If you want to only see projects from one of these sources, you can configure it in the Plugin settings.

## Development

```
git clone https://github.com/brpaz/vscode-projects
make link
```

The `make link` command will symlink the cloned repo into the appropriate location on the ulauncher extensions folder.

The `make link` command will symlink the cloned repo into the appropriate location on the ulauncher extensions folder.

To see your changes, stop ulauncher and run it from the command line with: `make dev`.

The output will display something like this:

```
2020-11-15 10:24:16,869 | WARNING | ulauncher.api.server.ExtensionRunner: _run_process() | VERBOSE=1 ULAUNCHER_WS_API=ws://127.0.0.1:5054/ulauncher-vscode-projects PYTHONPATH=/usr/lib/python3.8/site-packages /usr/bin/python3 /home/bruno/.local/share/ulauncher/extensions/ulauncher-vscode-projects/main.py
```

Open another terminal window and execute the command displayed, "starting at VERBOSE=1". This will activate the extension.

To see your changes, CTRL+C the previous command and run it again to refresh.

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 💛 Support the project

If this project was useful to you in some form, I would be glad to have your support.  It will help to keep the project alive and to have more time to work on Open Source.

The sinplest form of support is to give a ⭐️ to this repo.

You can also contribute with [GitHub Sponsors](https://github.com/sponsors/brpaz).

[![GitHub Sponsors](https://img.shields.io/badge/GitHub%20Sponsors-Sponsor%20Me-red?style=for-the-badge)](https://github.com/sponsors/brpaz)


Or if you prefer a one time donation to the project, you can simple:

<a href="https://www.buymeacoffee.com/Z1Bu6asGV" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>

## Author

👤 **Bruno Paz**

* Website: [brunopaz.dev](https://brunopaz.dev)
* Github: [@brpaz](https://github.com/brpaz)
* Twitter: [@brunopaz88](https://twitter.com/brunopaz88)

## License

Copywright @ 2019 [Bruno Paz](https://github.com/brpaz)

This project is [MIT](LLICENSE) Licensed.
