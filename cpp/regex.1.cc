#include <regex>

using namespace std;

int main(int argc, char** arg) {
	{
		regex rx(".*ll.*");
		bool match = regex_match("hello", rx);
	}
	{
		regex rx("lorem", regex_constants::icase);
		bool match = regex_match("Lorem", rx);
	}

}
