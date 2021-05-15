CREATE USER 'user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'sasa';

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'sasa';
ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY 'sasa';