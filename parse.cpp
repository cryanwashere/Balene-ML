#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <regex>


std::string remove_tag_content(const std:: string& html, const std::string& tagName)
{
    std::regex tagRegex("<" + tagName + "[^>]*>.*?<\\/" + tagName + ">");
    return std::regex_replace(html, tagRegex, "<" + tagName + "></" + tagName + ">");
}

std::string remove_html_tags(const std::string& html)
{
    std::regex tag_regex("<[^>]+>");
    std::string replaced = std::regex_replace(html, tag_regex, "");
    return replaced;
}

int main (int argc, char * argv[])
{
    std::ifstream file("file.html");
    std::string content;
    // Check if the file is open and ready for reading
    if (file.is_open()) {
        // Read the entire file content into a string
        content.assign((std::istreambuf_iterator<char>(file)),
                       (std::istreambuf_iterator<char>()));
        // Close the file
        file.close();
        std::cout << "File read operation completed successfully." << std::endl;
    } else {
        std::cout << "Unable to open the file for reading." << std::endl;
    }

    std::string parsed_output = content;

    parsed_output = remove_tag_content(parsed_output, "html");
    //parsed_output = remove_html_tags(parsed_output);


     // Write the tags to a new file.
    std::ofstream outfile("cleaned.html");
    if (outfile.is_open()) {
        // Write the content to the file
        outfile << parsed_output;
        // Close the file
        outfile.close();
        std::cout << "File write operation completed successfully." << std::endl;
    } else {
        std::cout << "Unable to open the file for writing." << std::endl;
    }

    return 0;
}