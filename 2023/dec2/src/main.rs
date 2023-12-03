use std::fs::File;
use std::io::{self, BufRead};

fn main() -> io::Result<()> {

    let file_path = "../Input/dec2";

    // Open the file
    let file = File::open(file_path)?;
    let reader = io::BufReader::new(file);
    let max_red = 12;
    let max_green = 13;
    let max_blue = 14;
    // Iterate over lines and print them
    let mut sum = 0;
    let mut power_sum = 0;
    for line in reader.lines() {
        match line {
            Ok(line) => {
                let mut max_found_red = 0;
                let mut max_found_green = 0;
                let mut max_found_blue = 0;
               // println!("{}", line);
                //extract the string between "Game " and ":"
                let game_number = &line[5..line.find(":").unwrap()];
                //parse into a number
                let game_number: u32 = game_number.parse().unwrap();
                //split the rest of the string into a vector of strings separated by ";"
                let mut sets: Vec<&str> = line[line.find(":").unwrap() + 2..].split(";").collect();
                //separate every set into a vector of strings separated by ","
                let mut allowed = true;

                for set in sets.iter_mut() {
                    let mut colors: Vec<&str> = set.split(",").collect();
                    //for every color
                    for color in colors.iter_mut() {
                        //remove the leading space
                        *color = color.trim_start();
                        //remove the trailing space
                        *color = color.trim_end();
                        //split the color into 2 parts, the number and the color
                        let mut color_parts: Vec<&str> = color.split(" ").collect();
                        //parse the number into a u32
                        let color_number: u32 = color_parts[0].parse().unwrap();
                        //check if the color is red
                        if color_parts[1] == "red" {
                            if(color_number > max_found_red)
                            {
                                max_found_red = color_number;
                            }
                            //if the number is greater than the max red
                            if color_number > max_red {
                                allowed = false;
                            }
                        }
                        //check if the color is green
                        if color_parts[1] == "green" {
                            if(color_number > max_found_green)
                            {
                                max_found_green = color_number;
                            }
                            //if the number is greater than the max green
                            if color_number > max_green {
                                allowed = false;
                            }
                        }
                        //check if the color is blue
                        if color_parts[1] == "blue" {
                            if(color_number > max_found_blue)
                            {
                                max_found_blue = color_number;
                            }
                            //if the number is greater than the max blue
                            if color_number > max_blue {
                                allowed = false;
                            }
                        }
                        
                    }                    
                }
                if allowed {
                    println!("Game {}: Allowed", game_number);
                    sum += game_number;
                } else {
                    println!("Game {}: Not Allowed", game_number);
                }
                //print the max found colors
                println!("Game {}: Max Red: {}, Max Green: {}, Max Blue: {}", game_number, max_found_red, max_found_green, max_found_blue);
                let power = max_found_red * max_found_green * max_found_blue;
                power_sum += power;
                
                
        },
            Err(e) => eprintln!("Error reading line: {}", e),
        }
    }
    println!("Sum: {}", sum);
    println!("Power Sum: {}", power_sum);
    Ok(())
}
