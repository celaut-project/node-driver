

from build.lib.dependency_manager.service_config import ServiceConfig


class ServiceInterface:
    
    def __init__(self, 
                 gateway_stub,
                 service_with_config: ServiceConfig
            ):
        
        self.gateway_stub = gateway_stub
        self.sc = service_with_config
        
    
    def __enter__(self):
        
        try:
            instance = self.sc.get_instance()
            
        except IndexError:
            instance = self.sc.launch_instance(self.gateway_stub)
            
        
        return instance
    
    
    def __exit__(self):
        pass
        