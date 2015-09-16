#include <iostream>

using namespace std;

class MedalCount {
	public:
		const char *country;
		int gold;
		int silver;
		int bronze;
};

int main(int argc, char** arg) {
	{
		typedef int customer_id;
		customer_id cid = 3;

		enum day_of_week { mon, tue, wed, thu, fri, sat, sun };
		day_of_week d = tue;

		MedalCount spain;
	}
	{
		MedalCount spain = { "Spain", 3, 7, 4 };
		spain.country = "Spain";
		spain.gold = 3;
		spain.silver = 7;
		spain.bronze = 4;
		int spain_total = spain.gold + spain.silver + spain.bronze;
	}
}
