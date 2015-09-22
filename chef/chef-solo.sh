### start of installation script ###


# download dependencies required to run app
sudo apt-get update
sudo apt-get install ruby-full -y
sudo apt-get install ruby-rack -y
sudo apt-get install git -y

# create working directory
mkdir /home/ubuntu
cd /home/ubuntu

#### install and configure chef ####

# create new directory for chef
mkdir /home/ubuntu/chef

cd chef
# download installation files to working ~/chef directory
wget https://www.opscode.com/chef/install.sh
ls
# run installation script
sudo sh install.sh
# check version
chef-solo -v
# set up project directory structure with wget master
wget http://github.com/opscode/chef-repo/tarball/master
tar -zxf master
# check default directory name
cd chef-chef-repo-e3efb8c/
cd ..
# rename folder for cleaner directory structure
mv chef-chef-repo-e3efb8c chef-repo
rm master
# cd cookbooks/
sudo mkdir .chef
sudo chown ubuntu:ubuntu .chef
sudo echo "cookbook_path ['/home/ubuntu/chef/chef-repo/cookbooks' ]" > .chef/knife.rb
# current directory /home/ubuntu/chef/chef-repo
cd chef-repo

#### additional packages for chef nginx and default dependencies

cd /home/ubuntu/chef/chef-repo/cookbooks

# chef cookbook nginx
knife cookbook site download nginx
tar zxf nginx*.tar.gz
rm nginx*.tar.gz

# chef cookbook apt
knife cookbook site download apt
tar zxf apt*
rm apt*.tar.gz

# chef cookbook build-essential
knife cookbook site download build-essential
tar zxf build*
rm build*.tar.gz

# chef cookbook bluepill
knife cookbook site download bluepill
tar zxf bluepill*
rm bluepill*.tar.gz

# chef cookbook rsyslog
knife cookbook site download rsyslog
tar zxf rsyslog*
rm rsyslog*.tar.gz

# chef cookbook runit
knife cookbook site download runit
tar zxf runit*
rm runit*.tar.gz

# chef cookbook ohai
knife cookbook site download ohai
tar zxf ohai*
rm ohai*.tar.gz

# chef cookbook yum
knife cookbook site download yum
tar zxf yum*
rm yum*.tar.gz

# chef cookbook yum-epel
knife cookbook site download yum-epel
tar zxf yum-epel*
rm yum-epel*.tar.gz

#### set up nginxapp chef default recipe cookbook

# create project nginxapp
knife cookbook create nginxapp

# change to nginxapp directory
cd /home/ubuntu/chef/chef-repo/cookbooks/nginxapp

# edit metadata.rb file
# sed metadata.rb ... depends nginx
sudo echo 'depends "nginx"' >> metadata.rb 

# edit default.rb
cd recipes
sudo touch default.rb
echo 'file_cache_path "/home/ubuntu/chef-solo"' > solo.rb
echo 'cookbook_path "/home/ubuntu/chef/chef-repo/cookbooks"' >> solo.rb

# create SOLO rb file for solo run

# change to chef repo directory
cd /home/ubuntu/chef/chef-repo

sudo touch solo.rb
echo 'file_cache_path "/home/ubuntu/chef-solo"' > solo.rb
echo 'cookbook_path "/home/ubuntu/chef/chef-repo/cookbooks"' >> solo.rb
sudo mkdir /home/ubuntu/chef-solo

# create JSON file for solo run
sudo touch web.json
echo '{' > web.json
echo '		"run_list": ["recipe[apt]", "recipe[nginxapp]"]' >> web.json
echo '}' >> web.json


### configure default.rb file for recipes

# link nginxapp to deploy recipe
cd /home/ubuntu/chef/chef-repo/cookbooks/nginxapp/recipes
echo 'include_recipe "nginx"' >> default.rb
echo '' >> default.rb
echo 'nginx_site "default" do' >> default.rb
echo ' enable true' >> default.rb
echo 'end' >> default.rb
echo '' >> default.rb
echo 'include_recipe "nginxapp::deploy"' >> default.rb

### build deploy recipe

touch deploy.rb
echo "#" >deploy.rb
echo "# Cookbook Name:: nginxapp" >> deploy.rb
echo "# Recipe:: deploy" >> deploy.rb
echo "#" >> deploy.rb
echo "" >> deploy.rb
echo "deploy_revision node['nginxapp']['deploy_dir'] do" >> deploy.rb
echo "  scm_provider Chef::Provider::Git" >> deploy.rb
echo "  repo node['nginxapp']['deploy_repo']" >> deploy.rb
echo "  revision node['nginxapp']['deploy_branch']" >> deploy.rb
echo "  enable_submodules true" >> deploy.rb
echo "  shallow_clone false" >> deploy.rb
echo "  action :deploy" >> deploy.rb
echo "  ignore_failure true" >> deploy.rb
echo "  restart_command do" >> deploy.rb
echo "    service "nginx" do action :restart; end" >> deploy.rb
echo "  end" >> deploy.rb
echo "end" >> deploy.rb

### build attribute file for deploy file
cd /home/ubuntu/chef/chef-repo/cookbooks/nginxapp/attributes
touch default.rb
echo "#" > default.rb
echo "# Cookbook Name:: nginxapp" >> default.rb
echo "# Attributes:: deploy" >> default.rb
echo "#" >> default.rb
echo "" >> default.rb
echo "default['nginxapp']['deploy_repo'] = 'git://github.com/triibal/hello.git'" >> default.rb
echo "default['nginxapp']['deploy_branch'] = 'master'" >> default.rb
echo "default['nginxapp']['deploy_dir'] = '/var/www/br'" >> default.rb
 
#### chef solo specific ################
#### run chef solo to install nginx ####

# make br directory
sudo mkdir /var/www
sudo mkdir /var/www/br
# chef convergence
cd /home/ubuntu/chef/chef-repo
sudo chef-solo -c solo.rb -j web.json



# configure nginx to reverse proxy to port 9292
# append nginx config files through bash 
# this could be more complete using chef attributes to modify nginx

sudo service nginx stop
sed '9 i\ proxy_pass http://127.0.0.1:9292;' /etc/nginx/sites-available/default > /etc/nginx/sites-available/new-default
cd /etc/nginx/sites-available/
sudo cp new-default default
sudo rm new-default
sudo service nginx restart

#### start ruby app ####

sudo setsid rackup config.ru


# navigate to directory of deployed app /var/www/br/releases/af97ea45a6d1a62733f61cd55717d4b93256f2ca 
# need to clean it up later!

# connect and test with localhost
curl localhost

#### END OF CURRENT SCRIPT ######

### NOTE
### requires manual nginx restart of nginx when not in vagrant
### currently debugging
### curl localhost working
