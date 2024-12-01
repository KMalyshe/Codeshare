public boolean validateCommand(String commandInput) {
        String[] command = commandInput.split(" ");
        command[0] = command[0].toUpperCase();

        switch (command[0]) {
            case "ADD":
                if (containsExtraArgs(command, 2)) {
                    return false;
                }
                try {
                    if (validateNumInput(command[1])) {
                    executeCommandWithArgs(Commands.ADD, Integer.valueOf(command[1]));
                    return true;
                    }
                    else {
                        throw new Exception();
                    }

                }
                catch (Exception e) {
                    ioHandler.printLine("Invalid Syntax. Syntax: ADD [n]");
                    return false;
                }
            case "DEL":
                if (containsExtraArgs(command, 2)) {
                    return false;
                }
                try {
                    if (validateNumInput(command[1])) {
                    executeCommandWithArgs(Commands.DEL, Integer.valueOf(command[1]));
                    return true;
                    }
                    else {
                        throw new Exception();
                    }
                }
                catch (Exception e) {
                    ioHandler.printLine("Invalid Syntax. Syntax: DEL [n]");
                    return false;
                }
            case "DUMMY":
                if (containsExtraArgs(command, 2)) {
                    return false;
                }
                try {
                    if (validateNumInput(command[1])) {
                    executeCommandWithArgs(Commands.DUMMY, Integer.valueOf(command[1]));
                    return true;
                    }
                    else {
                        throw new Exception();
                    }
                }
                catch (Exception e) {
                    ioHandler.printLine("Invalid Syntax. Syntax: DUMMY [n]");
                    return false;
                }
            case "EXIT":
                if (containsExtraArgs(command, 1)) {
                    return false;
                }
                executeCommand(Commands.EXIT);
                return true;  
            case "FORMAT":

            try {
                if (command[1].equalsIgnoreCase("FIX")) {
                    if (containsExtraArgs(command, 3)) {
                        return false;
                    }
                    try {
                        if (validateNumInput(command[2])) {
                            executeCommandWithArgs(Commands.FORMATFIX, Integer.valueOf(command[2]));
                            return true;
                        }
                        else throw new Exception();
                    }
                    catch (Exception e) {
                        ioHandler.printLine("Invalid Syntax. Syntax: FORMAT FIX [n]");
                        return false;
                    }
                }
                else if (command[1].equalsIgnoreCase("RAW")) {
                    if (containsExtraArgs(command, 2)) {
                        return false;
                    }
                    executeCommand(Commands.FORMATRAW);
                    return true;
                }
                else throw new Exception();
            }
            catch (Exception e) {
                ioHandler.printLine("Invalid Syntax. Syntax: FORMAT RAW or FORMAT FIX [n]");
                return false;
            }
            case "INDEX":
                if (containsExtraArgs(command, 1)) {
                    return false;
                }
                executeCommand(Commands.INDEX);
                return true;
            case "PRINT":
                if (containsExtraArgs(command, 1)) {
                    return false;
                }
                executeCommand(Commands.PRINT);
                return true;
            case "REPLACE":
                if (containsExtraArgs(command, 2)) {
                    return false;
                }
                try {
                    if (validateNumInput(command[1])) {
                    executeCommandWithArgs(Commands.REPLACE, Integer.valueOf(command[1]));
                    return true;
                    }
                    else {
                        throw new Exception();
                    }
                }
                catch (Exception e) {
                    ioHandler.printLine("Invalid Syntax. Syntax: REPLACE [n]");
                    return false;
                }
            default:
                ioHandler.printLine("Unrecognized command. Please try again.");
                return false;
        }
    }
