class MyHashMap {
public:
    int um[1000001];
    MyHashMap() {
        memset(um,-1,sizeof(um));
    }
    
    void put(int key, int value) {
        um[key]=value;
    }
    
    int get(int key) {
        return um[key];
    }
    
    void remove(int key) {
        um[key]=-1;
    }
};