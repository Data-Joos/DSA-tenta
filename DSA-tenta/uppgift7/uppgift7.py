def quicksort(arr, left, right): #left är från början 0 och right är slutet (len(arr)-1)
    if left < right: #Funktionen körs så länge vänster är mindre än höger.
        partition_pos = partition(arr, left, right) #Kalla på funktion nedan.
        #Recursion
        quicksort(arr, left, partition_pos - 1)
        quicksort(arr, partition_pos + 1, right)

    return arr

def partition(arr, left, right):#Returnerar pivot efter första quick-sorten så att första funktionen vet vart den ska splitta och sätta en ny pivot
    i = left #i går från vänster till höger o tittar efter ett element som > än pivot-elementet
    j = right - 1 #j går från höger till vänster o tittar efter ett element som < än pivot-elementet
    pivot = arr[right]

    while i < j: #i och j ska flyttas tills dom möts
        while i < right and arr[i] < pivot: #sålänge i är mindre än slutet på arrayn och elementet av i är mindre än pivot.
            i += 1 
        while j > left and arr[j] >= pivot: #sålänge j är större än början och elementet av index j är större eller lika med pivot
            j -= 1
        if i < j: #Kollar om dom korsat varandra
            arr[i], arr[j] = arr[j], arr[i] #Har dom inte det så byter vi plats på index i och index j.

    #Efter att i och korsats
    if arr[i] > pivot: #Om index i är större än pivot så måste den och pivot byta plats
        arr[i], arr[right] = arr[right], arr[i]
    
    return i


arr = [22, 11, 88, 66, 55, 77, 33, 44, 0]

print(quicksort(arr, 0, len(arr)-1))