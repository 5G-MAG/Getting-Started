---
layout: default
title: Guidelines for Contributors
parent: Introduction
nav_order: 1
---

<img src="../assets/images/Banner_RT.png" /> 

# About the Developer Community
* Meet the developer community, participate, contribute, join the public calls: [https://www.5g-mag.com/community](https://www.5g-mag.com/community)
* Discussions among developers are held in [Slack](https://5g-mag.slack.com/).
* Announcements are communicated through the [Google Group](https://groups.google.com/g/5g-mag-reference-tools)
* If you have questions which cannot be shared publicly, reach out to us via email: [reference-tools@5g-mag.com](mailto:reference-tools@5g-mag.com)

## Join our Public Monthly Call (Last Friday of the month at 13:00 CET/CEST - unless communicated otherwise)
* Find all the information about how to join the Public calls: [https://5g-mag.com/community#calendar](https://5g-mag.com/community#calendar)
* Agendas are circulated via the [Google Group](https://groups.google.com/g/5g-mag-reference-tools) mailing list

## Contributing

If you wish to contribute code to the projects then you will first need to send us a signed version of the **Contributor License Agreement (CLA)**.

Only individuals and/or companies with a signed CLA can contribute code. Please visit <https://www.5g-mag.com/license> for more details. The 5G-MAG Public License and CLAs can be downloaded from the following links:

* [5G-MAG Public License v1.0](http://5g-mag.github.io/Getting-Started/OFFICIAL_5G-MAG_Public_License_v1.0.pdf)
* [5G-MAG Individual Contributor License Agreement (CLA)](https://5g-mag.github.io/Getting-Started/OFFICIAL_5G-MAG_Contributor_License_Agreement.pdf)
* [5G-MAG Corporate Contributor License Agreement (CCLA)](https://5g-mag.github.io/Getting-Started/OFFICIAL_5G-MAG_Corporate_Contributor_License_Agreement.pdf)

<img src="../assets/images/projects/contributors.png" style="width: 80%">

# Guidelines for Contributors

## Raising Issues

Anyone can raise issues against projects, you do not need to have signed the Contributor License Agreement (CLA) to do so.

## Releases

### Release Process

**TODO: Details of the release process**
- Tagging for release candidates
- Period of RC testing (see [Testing release candidates](#testing-release-candidates))
- If there are blocking issues
  - Fix blockers
  - Create new release candidate
- ... otherwise
  - Package up the release
  - Announce the release on Slack and Google Groups

### Testing release candidates

Availability of a RC for testing is announned in the Google Group and/or during the 5G-MAG Developers Calls. Feedback can be provided via issues during the testing period.

## Git Branching strategy
We are using a slightly modified version of Gitflow as a branching model. A detailed introduction to Gitflow can be found [here](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow).

#### Main branch
The _main_ branch stores the official release history. The current version of the _main_ branch always stores the latest release.

#### Development branch
The _development_ branch serves as the integration branch for new feature and bugfix branches. It reflects the latest stable changes in the current development cycle.

#### Feature branches
Each new feature is implemented in a separate _feature_ branch. Feature branches use _development_ as their parent branch. When a feature is completed the respective branch gets merged back into development. 

A feature branch is created the following way:
````
git checkout development
git checkout -b feature/newfeature
````

#### Release branches
Once the _development_ branch has acquired enough features and bugfixes for a release, a release candidate branch is created based on the current version of the _development_ branch. For details on the release procedure please refer to the [release procedure](https://github.com/Dash-Industry-Forum/DASH-IF-Conformance/wiki/Release-Procedure) documentation.

The release candidate always includes a version number and is created in the following way:

````
git checkout develop
git checkout -b RC-1.2.0
````

Once a release candidate is approved the respective branch is merged into the _main_ branch.

#### Bugfix branches
Similar to _feature_ branches, the _bugfix_ branches are created directly from _development_. In contrast to hotfixes, bugfixes are not considered criticial and do not require a fast new release. _Bugfix_ branches are created the following way:

````
git checkout development
git checkout -b bugfix/newbugfix
````

#### Hotfix branches
_Hotfix_ branches are used to quickly patch production releases in case of critical errors. _Hotfix_ branches are created directly from _main_ and merged back into _main_ and _development_ as soon as they are completed. Once the hotfix is applied a new release shall be created.

````
git checkout main
git checkout -b hotfix/newhotfix
````

#### Cloning a repository with a specific branch
It is also possible to clone a repository and specify the target branch directly:

`git clone -b <branchname> <remote-repo-url>`

## Forking the project
To work on a new feature or a bugfix you first need to fork the repository that you want to work on. A detailed guide how to fork a repository can be found [here](https://docs.github.com/en/get-started/quickstart/fork-a-repo).

## Pull requests
Once a feature or a hotfix branch is completed a new pull request against the _development_ (in case of _feature_ branches) or the _main_ branch (in case of _hotfix_ branches) is created:

1.  Navigate to the list of available branches. Depending on the concrete setup the new branch is available directly on the main repository or on your fork of the main repository.

<img width="1233" alt="Bildschirmfoto 2022-03-22 um 14 30 29" src="https://user-images.githubusercontent.com/2427039/159494521-b5566dfc-0809-48a8-bc0e-071a69ec29ce.png">

2. Click on "New pull request"
<img width="1345" alt="Bildschirmfoto 2022-03-22 um 14 38 22" src="https://user-images.githubusercontent.com/2427039/159494412-57e45c2a-2e5d-4cb4-bb8c-dc45d14b82b6.png">

3. Select the target (base) branch:
   * For `feature` branches select the `development` branch
   * For `hotfix` branches select the `main` branch
4. Provide a summary of your changes in the textfield
5. Click on "Create pull request"
