echo ""
echo "Compiling -------------------------"
time g++ -g -o twitter twitter.cc -std=c++0x

echo ""
echo "Running ---------------------------"
time ./twitter > tweets.txt
