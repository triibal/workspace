#
# Cookbook Name:: nginx
# Recipe:: default
#
# Copyright 2015, YOUR_COMPANY_NAME
#
# All rights reserved - Do Not Redistribute

## Including the repo copy recipe
include_recipe 'nginx::updaterepo'

## Including the nginx package installation recipe
include_recipe 'nginx::packageinstall'

## Service resource to restart the nginx from other resource
service 'nginx' do
  supports :status => true, :restart => true, :reload => true
 end
