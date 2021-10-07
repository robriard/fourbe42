#! /bin/bash

function main(){
    case "$#" in
        0)
            if [[ -d ~/.fourbe42 ]]; then
                echo "fourbe42 is already installed"
            else
                git clone https://github.com/robriard/fourbe42.git ~/.fourbe42
                rm -rf ~/.fourbe42/.git ~/.fourbe42/*.sh
            fi
            python3 ~/.fourbe42/main.py
            ;;
        1)
            echo "Too many arguments"
            ;;
        esac
}