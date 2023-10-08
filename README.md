# Cookiecutter Research Project

Cookiecutter is a project to automate the generation of folder structures.
For example, starting a new research project.

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher):

```bash
pip install -U cookiecutter
```

Or, if you use `conda`:

```bash
pip install -U cookiecutter
```

Or, if you use `brew`:

```bash
brew install cookiecutter
```

Then, generate a Research Project Template by entering the following in your command line (Powershell or Terminal):

```bash
cookiecutter gh:jacobjameson/cookiecutter-project
```

You will be prompted for the following values:


Input Value        | Description
-------------------|----------------------------------------------------------------------------------------------------------------------------------------
`paper_title`      | Title of the paper. Example: "Academic Research Project"
`project_acronym`  | Acronym for the project, used as a short-hand for reference. Default: "ARP"
`full_name`        | Your full name, added to the Latex file. Other authors will have to be manually added to the Latex. Default: "Jacob Jameson"
`email`            | Your email address, added to the Latex file. Other authors will have to be manually added to the Latex. Default: "jacobjameson@g.harvard.edu"
`author_lastnames` | List of last names, used to name the folder of the project (separated by commas or spaces, can be ignored if `project_folder` is manually entered below). Default: "Jameson,Coots"
`project_folder`   | Folder to create the project in. Default: `project_acronym`_`author_lastnames`, e.g. "ARP_Jameson_Coots"
