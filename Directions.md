# Scientific Solutions Engineering Coding Challenge

One critical aspect of Flywheel’s mission is to facilitate reproducible science. This requires that researchers are able to fully utilize the platform for their analysis needs. To that end, part of the SSE’s role at Flywheel will be to code up existing research algorithms and tools in Gears for users to run within the platform. An equally important aspect of the SSE’s roll is help provide guidance to researchers regarding usage patterns and best practices of such Gears.

This challenge consists of two parts, which should require 3-6 hrs to complete. In the first part you will create a Flywheel Gear. In the second you will explain its usage in a Blog Post that will provide requisite information to prospective users to guide their usage of the Gear and explain what types of problems it can solve.

## Part 1: Build a Gear
Develop a Flywheel Gear comprising your favorite Neuroimaging tool.

### Requirements
- Familiarize yourself with the necessary concepts and follow standards and practices laid out in Flywheel’s Spec and Documentation pages:
    1. https://github.com/flywheel-io/gears/tree/master/spec
    2. https://docs.flywheel.io/hc/en-us/articles/360041766774-Gear-Building-Tutorial
- Your Gear should:
    1. Take at least 1 file as input (NIfTI or otherwise).
    2. Have no less than 2 configuration options listed in the `manifest.json` file. *Those options should be clearly referenced in the run script.*
    3. Outputs should consist of files that can be loaded with open-source software, or viewed within Flywheel (e.g., NIfTI).
    4. Run outside of Flywheel, using Docker. This means that you will have to provide sane defaults in the absence of user-input.

## Part 2: Communication
Provide a written summary of the Gear’s functionality and information regarding best practices. Format this summary as a Blog Post that is targeted at the broad user community. Your Post should be written at a level that would allow a person unfamiliar with Neuroimaging, or at least this tool, to decide when and how to implement the tool (i.e., what problem does it solve and how).

## Challenge deliverables
As a result of this challenge at least 4 files will be created.
1. `Dockerfile` - Describing how to build a container that will run your Gear
2. `run` - Python script that executes the tool.
3. `manifest.json` - JSON file that conforms to the Flywheel Gear Spec and provides all necessary information.
4. `Readme.md` - Markdown explaining the Gear’s usage.
