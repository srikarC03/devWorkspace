#include <SFML/Graphics.hpp>
#include <vector>
#include <string>
using namespace sf;
using namespace std;

class Tile{
    public:
        Tile(Texture &background, Texture &foreground, Texture &flag, float x, float y);
        void handleFlag();
        void update(map<string,Texture> &assets);
        void reveal(int &numTiles);
        void dbg();
        void draw(RenderWindow &window);

        bool isMine;
        bool debugMode;
        bool flagged;
        bool revealed;
        vector<Tile*> nbrs;
        int mineCount;
        string index;
    private:
        Sprite foreground;
        Sprite background;
        Sprite midground;
        Sprite flag;
};

Tile::Tile(Texture &background, Texture &foreground, Texture &flag, float x, float y){
    this->background.setTexture(background);
    this->foreground.setTexture(foreground);
    this->flag.setTexture(flag);

    this->flag.setColor(Color(255,255,255,0));

    this->background.setPosition(x,y);
    midground.setPosition(x,y);
    this->foreground.setPosition(x,y);
    this->flag.setPosition(x,y);
    mineCount = 0;
}

void Tile::handleFlag(){
    if(!revealed && !debugMode){
        if(flagged){
            flag.setColor(Color(255,255,255,0));
            flagged = false;
        }
        else{
            flag.setColor(Color(255,255,255,255));
            flagged = true;
        }
    }
}

void Tile::update(map<string,Texture> &assets){
    revealed = false;
    flagged = false;
    debugMode = false;
    foreground.setColor(Color(255,255,255,255));
    flag.setColor(Color(255,255,255,0));
    if(isMine){
        midground.setTexture(assets["mine"]);
    }
    else if(mineCount == 0){
        midground.setTexture(assets["tile_revealed"]);
    }
    else{
        String s = "number_" + to_string(mineCount);
        midground.setTexture(assets[s]);
    }

}

void Tile::reveal(int &numTiles){
    if(!revealed && !flagged){
        foreground.setColor(Color(255,255,255,0));
        revealed = true;
        if(!isMine){
            numTiles--;
        }
        if(!isMine && mineCount == 0){
            for(int i=0; i<nbrs.size(); i++){
                if(!nbrs[i]->isMine){
                    nbrs[i]->reveal(numTiles);
                }
            }
        }
    }
}

void Tile::dbg(){
    if(!revealed && isMine){
        if(debugMode){
            debugMode = false;
            if(flagged){
                flag.setColor(Color(255,255,255,255));
            }
            foreground.setColor(Color(255,255,255,255));   
        }
        else{
            debugMode = true;
            if(flagged){
                flag.setColor(Color(255,255,255,0));
            }
            foreground.setColor(Color(255,255,255,0));
        }
    }
}

void Tile::draw(RenderWindow &window){ 
    window.draw(background);
    window.draw(midground);
    window.draw(foreground);
    window.draw(flag);
}