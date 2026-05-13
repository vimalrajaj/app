#include <reg51.h>
void main(void) {
while(1) {
P2 = ~P2; // Toggle all bits of P2 continuously
}
}