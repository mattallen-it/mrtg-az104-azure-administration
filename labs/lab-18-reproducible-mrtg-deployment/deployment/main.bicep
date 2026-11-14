targetScope = 'resourceGroup'

param location string = 'centralus'

@allowed([
  'Lab'
  'Test'
])
param environment string = 'Lab'

param inboundRulePriority int = 1000

var commonTags = {
  Environment: environment
  Project: 'MRTG-AZ104-Administration'
  Lab: 'Lab-18'
  Owner: 'MRTG-Cloud-Operations'
}

var storageName = 'stl18${uniqueString(resourceGroup().id)}'

resource nsg 'Microsoft.Network/networkSecurityGroups@2023-11-01' = {
  name: 'nsg-mrtg-lab18-app'
  location: location
  tags: commonTags
  properties: {
    securityRules: [
      {
        name: 'Deny-All-Inbound'
        properties: {
          priority: inboundRulePriority
          direction: 'Inbound'
          access: 'Deny'
          protocol: '*'
          sourcePortRange: '*'
          destinationPortRange: '*'
          sourceAddressPrefix: '*'
          destinationAddressPrefix: '*'
        }
      }
    ]
  }
}

resource vnet 'Microsoft.Network/virtualNetworks@2023-11-01' = {
  name: 'vnet-mrtg-lab18'
  location: location
  tags: commonTags
  properties: {
    addressSpace: {
      addressPrefixes: [
        '10.180.0.0/16'
      ]
    }
    subnets: [
      {
        name: 'snet-app'
        properties: {
          addressPrefix: '10.180.10.0/24'
          networkSecurityGroup: {
            id: nsg.id
          }
        }
      }
    ]
  }
}

resource storage 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: storageName
  location: location
  tags: commonTags
  kind: 'StorageV2'
  sku: {
    name: 'Standard_LRS'
  }
  properties: {
    accessTier: 'Hot'
    supportsHttpsTrafficOnly: true
    minimumTlsVersion: 'TLS1_2'
    allowBlobPublicAccess: false
    allowSharedKeyAccess: false
    publicNetworkAccess: 'Disabled'
  }
}

output virtualNetworkName string = vnet.name
output networkSecurityGroupName string = nsg.name
output storageAccountName string = storage.name
output deployedEnvironment string = environment
