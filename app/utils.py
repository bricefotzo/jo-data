def create_color_from_str(value: bool = False) -> str:
    """
    Function to create a color from a 
    
    Args:
    - string: str

    Returns:
    - str

    Example:
    >>> create_color_from_str("France", 0.5)
    "rgba(X, Y, Z, 0.5)"

    """
    if value:
        return f"rgba(65, 184, 213, 1)"
    return f"rgba(65, 184, 213, 0.4)"