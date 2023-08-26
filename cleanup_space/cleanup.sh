
#copy everything below into space.sh and run it

# sudo rm -rf /tmp/*; # uncomment this line if you cant even run the following commands below

BEFORE1=`df -h | grep -i /dev/xvda1`;

sudo apt-get remove -y openjdk-11-jdk-headless;
sleep 1;
sudo apt-get remove -y openjdk-11-jre-headless;
sleep 1;
sudo apt-get remove -y mysql-server-core-5.7;
sleep 1;
sudo apt-get remove -y mysql-server-5.7;
sleep 1;
sudo apt-get remove -y mysql-server-5.7;
sleep 1;
sudo apt-get remove -y mysql-client-core-5.7;
sleep 1;
sudo apt-get remove -y mysql-client-5.7;
sleep 1;
sudo apt-get remove -y golang-1.9-go;
sleep 1;
sudo apt-get remove -y golang-1.9-src;
sleep 1;
sudo apt-get remove -y terraform;
sleep 1;
sudo apt-get remove -y gdb-dbg;
sleep 1;
sudo apt-get remove -y gcc-7;
sleep 1;
sudo apt-get remove -y g++-7;
sleep 1;
sudo apt-get remove -y gdb;
sleep 1;
sudo apt-get remove -y cpp-7;
sleep 1;
sudo apt-get remove -y libperl5.26;
sleep 1;
sudo apt-get remove -y perl-modules-5.26;
sleep 1;
sudo apt-get remove -y libstdc++-7-dev;
sleep 1;
sudo apt-get remove -y libpython2.7-dev;
sleep 1;
sudo apt-get autoremove -y;


AFTER1=`df -h | grep -i /dev/xvda1`;

echo "Used Space before: " $BEFORE1;
echo "Used Space after apt-get remove: " $AFTER1;
