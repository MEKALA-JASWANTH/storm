"""Sample Feature Module

This module demonstrates the extensibility of the STORM project.
It provides a basic example of how to add custom features and functionality
to the forked repository.

Author: MEKALA-JASWANTH
Date: November 2, 2025
"""

def sample_function(topic: str) -> dict:
    """
    A sample function that demonstrates basic functionality.
    
    This function takes a topic string and returns a dictionary
    with sample information about the topic.
    
    Args:
        topic (str): The topic to process
        
    Returns:
        dict: A dictionary containing sample information about the topic
        
    Example:
        >>> result = sample_function("Artificial Intelligence")
        >>> print(result['topic'])
        'Artificial Intelligence'
    """
    return {
        'topic': topic,
        'status': 'processed',
        'message': f'Sample processing completed for: {topic}',
        'features': ['feature1', 'feature2', 'feature3']
    }


def get_module_info() -> dict:
    """
    Returns information about this sample module.
    
    Returns:
        dict: Module information including name, version, and description
    """
    return {
        'name': 'sample_feature',
        'version': '1.0.0',
        'description': 'A sample module demonstrating STORM extensibility',
        'author': 'MEKALA-JASWANTH'
    }


if __name__ == '__main__':
    # Example usage
    print("Sample Feature Module")
    print("=" * 40)
    
    # Test the sample function
    result = sample_function("Knowledge Curation")
    print(f"Topic: {result['topic']}")
    print(f"Status: {result['status']}")
    print(f"Message: {result['message']}")
    print(f"Features: {', '.join(result['features'])}")
    
    print("\n" + "=" * 40)
    
    # Display module info
    module_info = get_module_info()
    print(f"Module: {module_info['name']} v{module_info['version']}")
    print(f"Description: {module_info['description']}")
    print(f"Author: {module_info['author']}")
