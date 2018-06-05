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
  <h2>installation</h2>
    <pre>
git clone https://github.com/robac/folderwatch
chmod +x folderwatch/install/ubuntu/install_ubuntu.sh
./folderwatch/install/ubuntu/install_ubuntu.sh
cp /etc/folderwatch/folderwatch.conf.sample /etc/folderwatch/folderwatch.conf</pre>
  <h2>run</h2>
    <pre>
systemctl enable folderwatch 
systemctl start folderwatch </pre>

  <h2>stop</h2>
    <pre>
systemctl stop folderwatch 
systemctl disable folderwatch </pre>

  
  
