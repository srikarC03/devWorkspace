#include <iostream>
#include <vector>
using namespace std;

class Image{
    public:
        // Structures needed for Image class
        struct Header{
            char idLength;
            char colorMapType;
            char dataTypeCode;
            short colorMapOrigin;
            short colorMapLength;
            char colorMapDepth;
            short xOrigin;
            short yOrigin;
            short width;
            short height;
            char bitsPerPixel;
            char imageDescriptor;
        };
        struct Pixel{
            unsigned char r;
            unsigned char g;
            unsigned char b;
            const unsigned char get(int i) const{
                if(i==0){return r;}
                else if(i==1){return g;}
                else if(i==2){return b;}
                return 0;
            }
            unsigned char get(int i){
                if(i==0){return r;}
                else if(i==1){return g;}
                else if(i==2){return b;}
                return 0;
            }
        };

        // Class member methods and constructor 
        Image(Header h){imgHeader = h;}
        const Pixel& operator[](unsigned int i) const{return imgData[i];}
        Pixel& operator[](unsigned int i){return imgData[i];}
        int length(){return imgData.size();}
        const Header getHeader() const{return imgHeader;}
        Header getHeader(){return imgHeader;}
        void add(Pixel& p){imgData.push_back(p);}

        bool operator==(Image& img){
            bool equal = true;

            if(imgHeader.bitsPerPixel!=img.getHeader().bitsPerPixel){
                equal = false;
            }
            if(imgHeader.colorMapDepth!=img.getHeader().colorMapDepth){
                equal = false;
            }
            if(imgHeader.colorMapLength!=img.getHeader().colorMapLength){
                equal = false;
            }
            if(imgHeader.colorMapOrigin!=img.getHeader().colorMapOrigin){
                equal = false;
            }
            if(imgHeader.colorMapType!=img.getHeader().colorMapType){
                equal = false;
            }
            if(imgHeader.dataTypeCode!=img.getHeader().dataTypeCode){
                equal = false;
            }
            if(imgHeader.height!=img.getHeader().height){
                equal = false;
            }
            if(imgHeader.width!=img.getHeader().width){
                equal = false;
            }
            if(imgHeader.idLength!=img.getHeader().idLength){
                equal = false;
            }
            if(imgHeader.imageDescriptor!=img.getHeader().imageDescriptor){
                equal = false;
            }
            if(imgHeader.xOrigin!=img.getHeader().xOrigin){
                equal = false;
            }
            if(imgHeader.yOrigin!=img.getHeader().yOrigin){
                equal = false;
            }
            if (length() != img.length()){
                equal=false;
            }
            
            if(equal)
            {
                for(int i=0; i<length(); i++){
                    for(int j=0; j<3; j++){
                        if(imgData[i].get(j)!=img[i].get(j)){
                            equal =false;
                        }
                    }
                }
            }
            return equal;
        }

        // Static methods for operating on images
        static Image Multiply(Image& a, Image& b){
            Image img = Image(a.getHeader());
            for(int i=0; i<a.length(); i++){
                Pixel A = a[i];
                Pixel B = b[i];
                unsigned char p[3];
                for(int j=0; j<3; j++){
                    p[j] = (unsigned char)(((A.get(j) * B.get(j)) / 255.0) + 0.5f);
                }
                Pixel C;
                C.r = p[0];
                C.g = p[1];
                C.b = p[2];
                img.add(C);
            }
            return img;
        }

        static Image Subtract(Image& a, Image& b){
            Image img = Image(a.getHeader());
            for(int i=0; i<a.length(); i++){
                Pixel A = a[i];
                Pixel B = b[i];
                unsigned char p[3];
                for(int j=0; j<3; j++){
                    if(B.get(j) - A.get(j)<=0){
                        p[j] = 0;
                    }
                    else{
                        p[j] = B.get(j) - A.get(j);
                    }
                }
                Pixel C;
                C.r = p[0];
                C.g = p[1];
                C.b = p[2];
                img.add(C);
            }
            return img;
        }

        static Image Screen(Image& a, Image& b){
            Image img = Image(a.getHeader());
            for(int i=0; i<a.length(); i++){
                Pixel A = a[i];
                Pixel B = b[i];
                unsigned char p[3];
                for(int j=0; j<3; j++){
                    p[j] = (unsigned char)((1 - (1 - A.get(j) / 255.0) * (1 - B.get(j) / 255.0)) * 255 + 0.5f);
                }
                Pixel C;
                C.r = p[0];
                C.g = p[1];
                C.b = p[2];
                img.add(C);
            }
            return img;
        }

        static Image Overlay(Image& a, Image& b){
            Image img = Image(a.getHeader());
            for(int i=0; i<a.length(); i++){
                Pixel A = a[i];
                Pixel B = b[i];
                unsigned char p[3];
                for(int j=0; j<3; j++){
                    if(B.get(j) / 255.0 <= 0.5){
                        float tmp =  2 * (A.get(j) / 255.0) * (B.get(j) / 255.0);
                        if(tmp>1){ 
                            tmp = 1;
                        }
                        p[j] = (unsigned char)(tmp * 255 +0.5f);
                    }
                    else{
                        float tmp = 1 - 2 * (1 - A.get(j) / 255.0) * (1 - B.get(j) / 255.0);
                        if(tmp<0){
                            tmp = 0;
                        }
                        p[j] = (unsigned char)(tmp * 255 + 0.5f);
                    }
                }
                Pixel C;
                C.r = p[0];
                C.g = p[1];
                C.b = p[2];
                img.add(C); 
            }
            return img;
        }
        
        static Image AddColor(Image& a, unsigned char r, unsigned char g, unsigned char b){
            Image img = Image(a.getHeader());
            for(int i=0; i<a.length(); i++){
                Pixel A = a[i];
                Pixel B;
                int tmp;
                tmp = A.get(0) + r;
                if(tmp > 255){tmp = 255;}
                B.r = (unsigned char)tmp;
                tmp = A.get(1) + g;
                if(tmp > 255){tmp = 255;}
                B.g = (unsigned char)tmp;
                tmp = A.get(2) + b;
                if(tmp > 255){tmp = 255;}
                B.b = (unsigned char)tmp;
                img.add(B);
            }
            return img;
        }

        static Image Scale(Image& a, int r, int g, int b){
            Image img = Image(a.getHeader());
            for(int i = 0; i<a.length(); i++){
                Pixel A = a[i];
                Pixel B;
                int tmp;
                tmp = A.get(0) * r;
                if(tmp>255){tmp = 255;}
                B.r = (unsigned char)tmp;
                tmp = A.get(1) * g;
                if(tmp>255){tmp = 255;}
                B.g = (unsigned char)tmp;
                tmp = A.get(2) * b;
                if(tmp>255){tmp = 255;}
                B.b = (unsigned char)tmp;
                img.add(B);
            }
            return img;
        }

        static vector<Image> Seperate(Image& a){
            vector<Image> colors;
            for(int i=0; i<3; i++){
                Image tmp = Image(a.getHeader());
                colors.push_back(tmp);            
            }

            for(int j=0; j<a.length(); j++){
                Pixel A = a[j];
                for(int k=0; k<3; k++){
                    Pixel tmp;
                    tmp.r = A.get(k);
                    tmp.g = A.get(k);
                    tmp.b = A.get(k);
                    colors[k].add(tmp);
                }
            }
            return colors;
        }

        static Image ColorCombine(Image& rc, Image& gc, Image& bc){
            Image img = Image(rc.getHeader());
            for(int i=0; i<rc.length(); i++){
                Pixel p;
                p.r = rc[i].r;
                p.g = gc[i].g;
                p.b = bc[i].b;
                img.add(p);
            }
            return img;
        }

        static Image Flip(Image& a){
            Header h = a.getHeader();
            Image img = Image(h);
            for(int i=h.width*h.height-1; i>=0; i--){
                Pixel p = a[i];
                img.add(p);
            }
            return img;
        }

        static Image Combine(Image& a, Image& b, Image& c, Image& d){
            Header h = a.getHeader();
            h.height*=2;
            h.width*=2;
            int x;
            Image img = Image(h);
            for(int i=0; i<h.height/2; i++){
                for(int j=0; j<h.width; j++){
                    if(j<h.width/2){
                        x = j + (h.width/2)*i;
                        Pixel p = d[x];
                        img.add(p);
                    }
                    else{
                        x = j + (h.width/2)*(i-1);
                        Pixel p = c[x];
                        img.add(p);
                    }
                }
            }
            for(int n=0; n<h.height/2; n++){
                for(int m=0; m<h.width; m++){
                    if(m<h.width/2){
                        x = m + (h.width/2)*n;
                        Pixel p = a[x];
                        img.add(p);
                    }
                    else{
                        x = m + (h.width/2)*(n-1);
                        Pixel p = b[x];
                        img.add(p);
                    }
                }
            }
            return img;
        }
    private:
        Header imgHeader;
        vector<Pixel> imgData;
};