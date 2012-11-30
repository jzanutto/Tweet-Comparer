#include <iostream>
#include <fstream>
#include <stdio.h>
#include <sstream>
#include <iomanip>
#include <ctype.h>
#include <string>
#include <vector>
#include <set>

using namespace std;

struct Tweet;

vector<Tweet> GetTweets(string fileName);
Tweet ExtractTweet(string line);

vector<string> SplitString(string input);
void GenerateDictionary();
bool ValidSpelling(string token);

string ParseWord(string input);
string StripURL(string input);
string StripNonAsciiChar(string input);
string Lowercase(string input);

static set<string> dictionary;

//---------------------------------------------------------------------------------
// Tweet
//---------------------------------------------------------------------------------

struct Tweet
{
    int correctSpelling;
    string originalTweet;
    vector<string> words;
    vector<string> incorrectlySpelledWords;

    Tweet(string tweet);
    string GetTweet();
};

Tweet::Tweet(string tweet)
{
    originalTweet   = tweet;
    correctSpelling = 0;

    vector<string> tokens = SplitString(tweet);

    for (int i = 0; i < tokens.size(); ++i)
    {
        string word = ParseWord(tokens[i]);

        if (!word.empty())
        {
            words.push_back(word);
        }
    }

    for (int i = 0; i < words.size(); ++i)
    {
        if (ValidSpelling(words[i]))
        {
            correctSpelling++;
        }
        else
        {
            incorrectlySpelledWords.push_back(words[i]);
        }
    }
}

string Tweet::GetTweet()
{
    stringstream ss;

    for (int i = 0; i < words.size(); ++i)
    {
        ss << words[i] << " ";
    }

    return ss.str();
}

//---------------------------------------------------------------------------------
// Actual Parsing
//---------------------------------------------------------------------------------

vector<Tweet> GetTweets(string fileName)
{
    ifstream tweetFile;
    tweetFile.open(fileName.c_str(), ifstream::in);

    vector<Tweet> tweets;
    string line;
    getline(tweetFile, line); // clear title row

    while (!tweetFile.fail())
    {
        line = "";
        getline(tweetFile, line);

        if (!line.empty())
        {
            tweets.push_back(ExtractTweet(line));
        }
    }

    return tweets;
}

Tweet ExtractTweet(string line)
{
    stringstream ss;
    ss << line;

    string token;
    getline(ss, token, ','); // skip tweet id
    getline(ss, token, ','); // skip username
    getline(ss, token, ','); // get actual tweet

    return token.substr(1, token.size() - 2); // strip quotes
}

string ParseWord(string token)
{
    // return invalid if is:
    //      - reply
    //      - url
    //      - RT (retweet) keyword
    if (token.substr(0, 1) == "@" || 
        token.substr(0, 7) == "http://" ||
        token == "RT" || token.substr(0,1)=="#" ||
        token.substr(0,1)==":" ||
        token.substr(0,1)=="=")
    {
        return "";
    }

    token = Lowercase(token);
    token = StripNonAsciiChar(token);

    return token;
}

string Lowercase(string input)
{
    string output;

    for (int i = 0; i < input.size(); ++i)
    {
        output += tolower(input[i]);
    }

    return output;
}

string StripNonAsciiChar(string input)
{
    stringstream ss;

    for (int i = 0; i < input.size(); ++i)
    {
        if (input[i] >= 'a' && input[i] <= 'z' || input[i] == ' ')
        {
            ss << input[i];
        }
    }

    return ss.str();
}

//---------------------------------------------------------------------------------
// Helper Functions
//---------------------------------------------------------------------------------

vector<string> SplitString(string input)
{
    stringstream ss(input);

    string buffer;
    vector<string> terms;

    while (ss >> buffer)
    {
        terms.push_back(buffer);
    }

    return terms;
}

void GenerateDictionary()
{
    ifstream dictFile;
    dictFile.open("dict-v2.txt", ifstream::in);

    string line;        

    while (!dictFile.fail())
    {
        getline(dictFile, line);

        if (!line.empty())
        {
            dictionary.insert(Lowercase(line));
        }
    }
}

/**
 * return false if not in dictionary
 */
bool ValidSpelling(string token)
{
    // found in dictionary
    if (dictionary.find(token) != dictionary.end())
    {
        return true;
    }

    // check last letter to see if it's an 's'
    // if so need to check if it's a plural
    if (token[token.size() - 1] == 's')
    {
        string singular = token.substr(0, token.size() - 2);

        if (dictionary.find(singular) != dictionary.end())
        {
            return true;
        }
    }

    return false;
}

//---------------------------------------------------------------------------------
// Main
//---------------------------------------------------------------------------------

int main()
{
    GenerateDictionary();

    vector<Tweet> swagTweets = GetTweets("#SWAG_tweets_2012_11_29.csv");
    vector<Tweet> yoloTweets = GetTweets("#YOLO_tweets_2012_11_29.csv");

    cerr << endl;
    cerr << setw(12) << "Dictionary: " << dictionary.size() << endl;
    cerr << setw(12) << "#swag: " << swagTweets.size() << endl;
    cerr << setw(12) << "#yolo: " << yoloTweets.size() << endl;
    int totalWrong = 0;
    int incorrectSwag = 0;
    int incorrectYOLO = 0;
    for (int i = 0; i < swagTweets.size(); ++i)
    {
        cout << setw(20) << "Original Tweet: " << swagTweets[i].originalTweet << endl;
        cout << setw(20) << "Parsed Tokens: " << swagTweets[i].GetTweet() << endl;
        cout << setw(20) << "Correct Words: " << swagTweets[i].correctSpelling << endl;
        cout << setw(20) << "Incorrect Words: " << endl;
        int j = 0;
        for (; j < swagTweets[i].incorrectlySpelledWords.size(); ++j)
        {
            cout << setw(20) << " " << swagTweets[i].incorrectlySpelledWords[j] << endl;
            totalWrong++;
        }
        incorrectSwag+=j;
        cout << endl;
    }
    for (int i = 0; i < yoloTweets.size(); ++i)
    {
        cout << setw(20) << "Original Tweet: " << yoloTweets[i].originalTweet << endl;
        cout << setw(20) << "Parsed Tokens: " << yoloTweets[i].GetTweet() << endl;
        cout << setw(20) << "Correct Words: " << yoloTweets[i].correctSpelling << endl;
        cout << setw(20) << "Incorrect Words: " << endl;
        int j = 0;
        for (; j < yoloTweets[i].incorrectlySpelledWords.size(); ++j)
        {
            cout << setw(20) << "Original Tweet: " << yoloTweets[i].incorrectlySpelledWords[j] << endl;
            totalWrong++;
        }
        incorrectYOLO+=j;
        cout << endl;
    }
    cerr << "Total incorrectness in swag: " << incorrectSwag << endl;
    cerr << "Total incorrectness in YOLO: " << incorrectYOLO << endl;
    cerr << "Total spelling mistakes: " << totalWrong << endl;
}
