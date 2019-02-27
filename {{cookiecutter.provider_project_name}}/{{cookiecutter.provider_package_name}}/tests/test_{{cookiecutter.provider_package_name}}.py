import pytest
import pytest
import os

import {{cookiecutter.provider_package_name}}
from merceedge.util.yaml import load_yaml
from merceedge.util.mock import MockEdge, gen_test_loop
from merceedge.core import (
    Component,
    Output,
    Input
)

mock_edge = MockEdge({{cookiecutter.provider_package_name}}.__config__)

@pytest.mark.run(order=1)
@gen_test_loop(mock_edge)
async def test_{{cookiecutter.provider_package_name}}():
   
    test_config = {{cookiecutter.provider_package_name}}.__config__
   
    new_provider_obj = {{cookiecutter.provider_class_name}}(edge=mock_edge,
                                                            config=test_config)

    """
     1. Test async setup
     2. Test conn_output_sink
     3. Test conn_input_slot
     3. Test emit_input_slot
     4. Test stop provider
    """
    # 1. Test asnyc setup
    attrs = {}
    await new_provider_obj.async_setup(mock_edge, attrs)

    # 2. Test conn_output_sink
    mock_component = Component(mock_edge, {})
    mock_output = Output(mock_edge, "test_output", mock_component)
    def output_sink_callback(payload):
        print(payload)
        # TODO assert ..
    await new_provider_obj.conn_output_sink(mock_output, {}, output_sink_callback)

    # 3. Test conn_input_slot
    mock_input = Input(mock_edge, "test_input", mock_component)
    await new_provider_obj.conn_input_slot(mock_input, {})
    # TODO assert new_provider_obj ...

    # 4. Test emit_input_slot
    payload = {}
    await new_provider_obj.emit_input_slot(mock_input, payload)
    # TODO assert new_provider_obj ...
    
    # 5. Test stop provider
    # TODO await new_provider_obj.stop ...




    
    
   

    
    

        
