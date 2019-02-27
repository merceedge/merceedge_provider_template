from merceedge.providers.base import ServiceProvider


class {{cookiecutter.provider_class_name}}(ServiceProvider):
    name = '{{cookiecutter.provider_class_name}}'
    """
    Author: {{cookiecutter.author}}
    License:{{cookiecutter.license}}
    Description:{{cookiecutter.description}}
    """
    def __init__(self, edge, config):
        """
        edge: MerceEdge instance
        config: user config
        """
        super({{cookiecutter.provider_class_name}}, self).__init__(edge, config)
    
    async def async_setup(self, edge, config):
        raise NotImplementedError
    
    async def conn_output_sink(self, output, output_wire_params, callback):
        # Subscribe callback -> EventBus -> Wire input (output sink ) -> EventBus(Send) -> Service provider  
        raise NotImplementedError

    async def conn_input_slot(self, input, input_wire_params):
        """connect input interface on wire input slot """
        pass
    
    async def emit_input_slot(self, input, payload):
        """send data to input slot"""
        raise NotImplementedError

    async def disconn_output_sink(self, output):
        """ disconnect wire output sink
        """
        raise NotImplementedError