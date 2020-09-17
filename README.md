# Toy Robot Challenge

The Toy Robot is a CLI application that simulates a toy robot moving on a square table top, of dimensions 5 units x 5 units.
 
There are no other obstructions on the table surface and the robot is free to roam around the surface of the table, 
but must be prevented from falling to destruction.
 
Any movement that would result in the robot falling from the table must be prevented, however further valid movement commands must still be allowed.

The allowed moves are:

* **PLACE X,Y,F:** The robot is placed on the table on position (X,Y) facing direction F (NORTH, SOUTH, EAST, WEST)

    E.g.: `PLACE 0,0,NORTH`


* **MOVE:** The robot moves 1 position towards the current facing direction

    E.g.:
    ```
    PLACE 0,0,NORTH
    MOVE
    ```
    Robot will move to position (0,1,NORTH)


* **LEFT:** The robot rotates to the left of the current direction without changing positions.

    E.g.: 
    ```
    PLACE 0,0,NORTH
    LEFT
    ```
    Robot will rotate and start facing WEST.


* **RIGHT:** The robot rotates to the right of the current direction without changing positions.

    E.g.: 
    ```
    PLACE 0,0,NORTH
    RIGHT
    ```

    Robot will rotate and start facing EAST.


* **REPORT:** Print the current robot position
    
    E.g.:
    ```
    PLACE 0,0,NORTH
    REPORT
    ```
    
    Robot will print 0,0,NORTH.
     
    **OBS:** If robot is outside boundaries an empty line is printed.


### How does it work?

To enable the robot, an initial 'PLACE' commands is required  with proper coordinates and direction,
and the robot will not respond to any command before the initial 'PLACE' command.

The robot only works within the boundaries that are defined by an imaginary square of fixed size 5X5, starting from
(0,0) up to (4,4).

Once the robot is placed in a valid position any subsequent command will be issued to the robot,
but any command that moves the robot outside its limits will be ignored, including another 'PLACE' command.

## Requirements

The CLI is written in <a href="https://www.python.org/downloads/release/python-380/" target="_blank">Python3.8</a>.
 
* <a href="https://pipenv-fork.readthedocs.io/en/latest/" target="_blank">Pipenv</a> to manage the virtualenv + install packages
* <a href="https://click.palletsprojects.com/en/7.x/" target="_blank">Click</a> to manage the command line 
* <a href="https://docs.pytest.org/en/stable/" target="_blank">Pytest</a> to execute unit tests


# How to install

To install the application is just a matter of running one command, by first you need to make sure
all the installation dependencies are resolved.

## Dependencies

The CLI and its dependencies are fully containerized and rely on Docker and Docker-compose to manage 
the containers and uses of Make as our build automation tool.

So, if you don't have them installed already, please follow the links below:

* <a href="https://www.docker.com/" target="_blank">Docker</a> - Instructions to <a href="https://docs.docker.com/get-docker/" target="_blank">install</a>

* <a href="https://docs.docker.com/compose/" target="_blank">Docker Compose</a> - Instruction to <a href="https://docs.docker.com/compose/install/" target="_blank">install</a>

* <a href="https://en.wikipedia.org/wiki/Make_%28software%29" target="_blank">Make</a>


## Installation

Once the dependencies are installed, just follow the simple steps below to have the CLI up and running.

Clone the repo and change the directory to the newly cloned folder.

```bash
git clone https://github.com/lmagalhaes/toy-robot.git
cd toy-robot
```
 
Use the command `make install` to trigger the installation.

```
make install 
```

The `make install` command build images, configure, and install the application.


*Obs:* You can simply run `make` or `make help` for a list of all available commands.

 
# Starting the robot
To start communicating with the robot just run `make start`

It will run the container in interactive move, and will prompt you to start sending commands.

To exit press CTRL+C, at any time.


# Warm-up
The warm-up command is a way to send commands to the robot automatically.
All issued commands will be output to the console, so you know what is going on.

To warm-up the robot, run `make warm-up`.

All the commands issued to the robot can be on the file [`robot_warmup.txt`](resources/robot_warmup.txt), inside the [`resources`](resources) folder.

Feel free to edit the file to add and remove commands and all changes will be reflected inside the container
 
# Running unit tests
To run the unit tests, simply run `make test`.

It will use run the testing container and trigger the `pytest` command.

After the tests finish running, you can check the coverage by opening `coverage/index.html` in the browser.

The coverage/index.html can be found on the root folder.


# Console

If you want to log-in into the container and play with the CLI, run  `make console`.

```
make console
root@fa1950e80dc0:/opt/toy_robot# toy-robot --version
toy-robot, version 1.0.0
root@fa1950e80dc0:/opt/toy_robot# exit
```

To exit the container, press CTRL+D, at any time.

## Uninstall

To uninstall run `make uninstall` the remove all images.
Than change to the directory outside the project and delete it.

```
make uninstall
```

Then, move out of the `toy-robot` directory and delete it.
```
cd ..
rm -rf toy-robot
```
