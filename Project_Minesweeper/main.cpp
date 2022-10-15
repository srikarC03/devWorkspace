#include <SFML/Graphics.hpp>
#include "Board.h"
#include <iostream>
using namespace std;
using namespace sf;

int main(){
    Board ms;
    RenderWindow window(VideoMode(ms.width*32,ms.height*32+64),"Minesweeper");

    while(window.isOpen()){
        Event event;
        
        while(window.pollEvent(event)){
            if(event.type == Event::Closed){
                window.close();
            }
            
            window.clear(Color(255,255,255,255));
            ms.update(window);
            window.display();

        }

    }
    return 0;
}    
