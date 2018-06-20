# folderwatch
inotifywait foldrer watch service for systemd

<h2>prerequisities</h2>
  <ul>
    <li>inotifywait</li>
    <li>Python</li>    
      <ul>
        <li>PyYAML</li>
        <li><i>(optional)</i> MySQLdb</li>
      </ul>  
    <li><i>(optional)</i> MySQL/MariaDB</li>
  </ul>
  <h2>installation (Ubuntu / Centos)</h2>
    <pre>
git clone https://github.com/robac/folderwatch
#Ubuntu
chmod +x folderwatch/install/ubuntu/install_ubuntu.sh
./folderwatch/install/ubuntu/install_ubuntu.sh

#Centos
chmod +x folderwatch/install/centos/install_centos.sh
./folderwatch/install/centos/install_centos.sh
cp /etc/folderwatch/folderwatch.conf.sample /etc/folderwatch/folderwatch.conf</pre>
  <h2>run</h2>
    <pre>
systemctl enable folderwatch 
systemctl enable ./folderwatch/src/systemd/folderwatch.service
systemctl start folderwatch </pre>

  <h2>stop</h2>
    <pre>
systemctl stop folderwatch 
systemctl disable folderwatch </pre>

  
  
