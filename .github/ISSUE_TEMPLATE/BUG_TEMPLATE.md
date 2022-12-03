---
name: 🐛 Bug report
about: File a bug report here
title: "[BUG]: "
labels: ["Issue-Bug", "Needs-Triage"]
assignees: ["DOS1986"]
---
body:
  - type: markdown
    attributes:
      value: |
        **Thank you for wanting to report a bug in ECPKeeper!**

        ⚠ Please make sure that this [issue wasn't already requested][issue search], or already implemented in the main branch.

        [issue search]: https://github.com/ecpkeeper/ECPKeeper/issues?q=is%3Aissue+is%3Aopen+
      options:
      - label: I have searched the existing issues
        required: true
  - type: textarea
    id: what-happened
    attributes:
      label: Bug Description
      description:
        What is the bug about? Please give a brief description of what happened and what should've happened.
      placeholder:
    validations:
      required: true
  - type: textarea
    id: steps-to-reproduce
    attributes:
      label: Steps To Reproduce
      description: Steps to reproduce the behavior.
      placeholder: |
        1. Go to '...'
        2. Click on '...'
        3. Scroll down to '...'
        4. See error
    validation: true
  - type: textarea
    id: additional-information
    attributes:
      label:  Additional Information
      description:  Provide any additional information such as logs, screenshots, likes, scenarios in which the bug occurs so that it facilitates resolving the issue.
    validations:
      required: true
  - type: textarea
    id: application-version
    attributes:
      label: ECPKeeper version
      description: Please enter the version.
      placeholder: |
        ECPKeeper 0.1
    validations:
      required: true
  - type: dropdown
    id: operating-system
    attributes:
      label: Windows build number
      Description: If this issue is occurring on more than 1 operating system, select the appropriate operating system.
      multiple: true
      options:
        - Other
        - Windows
        - Linux
        - Mac OS
    validations:
      required: true
  - type: textarea
    attributes:
      label: OS Version
      description: >-
        Provide all relevant information below, e.g. OS version etc.
      placeholder: Fedora 33, Cygwin, Windows 10, Windows XP, Mac OS 9.10 etc.